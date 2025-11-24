import ssl
import socket
from datetime import datetime
from cryptography import x509
from cryptography.hazmat.backends import default_backend
import OpenSSL

class SSLAnalyzer:
    def __init__(self, hostname, port=443, timeout=5):
        self.hostname = hostname
        self.port = port
        self.timeout = timeout
        self.cert_pem = None
        self.cert_dict = None
        self.x509_cert = None
    
    def get_certificate(self):
        """Fetch SSL certificate from the server"""
        try:
            # Create SSL context
            context = ssl.create_default_context()
            
            # Connect and get certificate
            with socket.create_connection((self.hostname, self.port), timeout=self.timeout) as sock:
                with context.wrap_socket(sock, server_hostname=self.hostname) as ssock:
                    # Get certificate in DER format
                    cert_der = ssock.getpeercert(binary_form=True)
                    # Get certificate as dictionary
                    self.cert_dict = ssock.getpeercert()
                    
                    # Convert to PEM format
                    self.cert_pem = ssl.DER_cert_to_PEM_cert(cert_der)
                    
                    # Parse with cryptography library
                    self.x509_cert = x509.load_der_x509_certificate(cert_der, default_backend())
                    
            return True
        except socket.gaierror:
            print(f"❌ Error: Unable to resolve hostname '{self.hostname}'")
            return False
        except socket.timeout:
            print(f"❌ Error: Connection timeout to {self.hostname}:{self.port}")
            return False
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            return False
    
    def get_basic_info(self):
        """Extract basic certificate information"""
        if not self.cert_dict:
            return None
        
        info = {
            'subject': dict(x[0] for x in self.cert_dict.get('subject', [])),
            'issuer': dict(x[0] for x in self.cert_dict.get('issuer', [])),
            'version': self.cert_dict.get('version'),
            'serial_number': self.cert_dict.get('serialNumber'),
            'not_before': self.cert_dict.get('notBefore'),
            'not_after': self.cert_dict.get('notAfter'),
        }
        return info
    
    def get_validity_info(self):
        """Check certificate validity and expiry"""
        if not self.x509_cert:
            return None
        
        not_before = self.x509_cert.not_valid_before
        not_after = self.x509_cert.not_valid_after
        now = datetime.utcnow()
        
        is_valid = not_before <= now <= not_after
        days_to_expire = (not_after - now).days
        
        return {
            'not_before': not_before.strftime('%Y-%m-%d %H:%M:%S UTC'),
            'not_after': not_after.strftime('%Y-%m-%d %H:%M:%S UTC'),
            'is_valid': is_valid,
            'days_to_expire': days_to_expire,
            'expired': days_to_expire < 0
        }
    
    def get_subject_alternative_names(self):
        """Extract Subject Alternative Names (SANs)"""
        if not self.x509_cert:
            return []
        
        try:
            san_extension = self.x509_cert.extensions.get_extension_for_class(
                x509.SubjectAlternativeName
            )
            return [dns.value for dns in san_extension.value]
        except x509.ExtensionNotFound:
            return []
    
    def get_public_key_info(self):
        """Extract public key information"""
        if not self.x509_cert:
            return None
        
        public_key = self.x509_cert.public_key()
        key_type = type(public_key).__name__
        
        info = {'type': key_type}
        
        if hasattr(public_key, 'key_size'):
            info['size'] = public_key.key_size
        
        return info
    
    def get_signature_algorithm(self):
        """Get certificate signature algorithm"""
        if not self.x509_cert:
            return None
        
        return self.x509_cert.signature_algorithm_oid._name
    
    def analyze_security(self):
        """Perform basic security analysis"""
        security_issues = []
        
        validity = self.get_validity_info()
        if validity:
            if validity['expired']:
                security_issues.append("⚠️  Certificate has EXPIRED")
            elif validity['days_to_expire'] < 30:
                security_issues.append(f"⚠️  Certificate expires soon ({validity['days_to_expire']} days)")
        
        pub_key = self.get_public_key_info()
        if pub_key and pub_key.get('size'):
            if pub_key['size'] < 2048:
                security_issues.append(f"⚠️  Weak key size: {pub_key['size']} bits (recommended: 2048+)")
        
        sig_algo = self.get_signature_algorithm()
        if sig_algo and 'sha1' in sig_algo.lower():
            security_issues.append("⚠️  Using weak SHA-1 signature algorithm")
        
        return security_issues if security_issues else ["✅ No major security issues detected"]