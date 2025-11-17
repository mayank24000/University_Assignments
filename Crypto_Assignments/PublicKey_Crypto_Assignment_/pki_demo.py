#!/usr/bin/env python3
"""
Q3: Public Key Infrastructure (PKI) Simulation - Enhanced with debugging
"""

from cryptography import x509
from cryptography.x509.oid import NameOID, ExtensionOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
import datetime
import os
import sys
import traceback

# Optional colorama with fallback
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    HAS_COLOR = True
except ImportError:
    HAS_COLOR = False
    class Fore:
        CYAN = YELLOW = GREEN = RED = MAGENTA = ''
    class Style:
        BRIGHT = ''

class PKISimulator:
    """Simulate basic PKI operations"""
    
    def __init__(self):
        self.ca_key = None
        self.ca_cert = None
        
        # Get absolute path for certificates directory
        self.cert_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "certificates")
        
        # Debug: Show where we're trying to save certificates
        print(f"{Fore.YELLOW}Certificate directory: {self.cert_dir}")
        print(f"{Fore.YELLOW}Current working directory: {os.getcwd()}")
        
        # Create directory with error handling
        try:
            if not os.path.exists(self.cert_dir):
                os.makedirs(self.cert_dir)
                print(f"{Fore.GREEN}✓ Created certificates directory: {self.cert_dir}")
            else:
                print(f"{Fore.GREEN}✓ Certificates directory already exists: {self.cert_dir}")
            
            # Test write permissions
            test_file = os.path.join(self.cert_dir, "test_write.txt")
            with open(test_file, 'w') as f:
                f.write("test")
            os.remove(test_file)
            print(f"{Fore.GREEN}✓ Write permissions verified for certificates directory")
            
        except PermissionError as e:
            print(f"{Fore.RED}✗ Permission denied creating/accessing directory: {e}")
            print(f"{Fore.RED}  Try running with administrator privileges or choose a different directory")
            sys.exit(1)
        except Exception as e:
            print(f"{Fore.RED}✗ Error creating certificates directory: {e}")
            traceback.print_exc()
            sys.exit(1)
    
    def create_ca_certificate(self):
        """Create a Certificate Authority (CA) certificate"""
        print(f"\n{Fore.CYAN}Creating Certificate Authority (CA)...")
        
        try:
            # Generate CA private key
            print(f"{Fore.YELLOW}  Generating 4096-bit RSA key...")
            self.ca_key = rsa.generate_private_key(
                public_exponent=65537,
                key_size=4096,
                backend=default_backend()
            )
            print(f"{Fore.GREEN}  ✓ CA private key generated")
            
            # Create CA certificate
            subject = issuer = x509.Name([
                x509.NameAttribute(NameOID.COUNTRY_NAME, "IN"),
                x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "Delhi"),
                x509.NameAttribute(NameOID.LOCALITY_NAME, "New Delhi"),
                x509.NameAttribute(NameOID.ORGANIZATION_NAME, "Demo CA Authority"),
                x509.NameAttribute(NameOID.COMMON_NAME, "Demo Root CA"),
            ])
            
            # Use timezone-aware datetime
            now = datetime.datetime.now(datetime.timezone.utc)
            
            print(f"{Fore.YELLOW}  Building CA certificate...")
            self.ca_cert = (
                x509.CertificateBuilder()
                .subject_name(subject)
                .issuer_name(issuer)
                .public_key(self.ca_key.public_key())
                .serial_number(x509.random_serial_number())
                .not_valid_before(now)
                .not_valid_after(now + datetime.timedelta(days=3650))
                .add_extension(
                    x509.BasicConstraints(ca=True, path_length=None),
                    critical=True,
                )
                .add_extension(
                    x509.KeyUsage(
                        key_cert_sign=True,
                        crl_sign=True,
                        digital_signature=False,
                        content_commitment=False,
                        key_encipherment=False,
                        data_encipherment=False,
                        key_agreement=False,
                        encipher_only=False,
                        decipher_only=False,
                    ),
                    critical=True,
                )
                .sign(self.ca_key, hashes.SHA256(), backend=default_backend())
            )
            print(f"{Fore.GREEN}  ✓ CA certificate created")
            
            # Save CA certificate and key
            ca_cert_path = os.path.join(self.cert_dir, "ca_certificate.pem")
            ca_key_path = os.path.join(self.cert_dir, "ca_private_key.pem")
            
            # Save certificate
            print(f"{Fore.YELLOW}  Saving CA certificate to {ca_cert_path}...")
            with open(ca_cert_path, "wb") as f:
                cert_bytes = self.ca_cert.public_bytes(serialization.Encoding.PEM)
                f.write(cert_bytes)
                print(f"{Fore.GREEN}  ✓ Written {len(cert_bytes)} bytes")
            
            # Verify certificate was saved
            if os.path.exists(ca_cert_path):
                file_size = os.path.getsize(ca_cert_path)
                print(f"{Fore.GREEN}✓ CA Certificate saved successfully: {ca_cert_path} ({file_size} bytes)")
            else:
                print(f"{Fore.RED}✗ Failed to save CA certificate!")
            
            # Save private key
            print(f"{Fore.YELLOW}  Saving CA private key to {ca_key_path}...")
            with open(ca_key_path, "wb") as f:
                key_bytes = self.ca_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.TraditionalOpenSSL,
                    encryption_algorithm=serialization.NoEncryption()
                )
                f.write(key_bytes)
                print(f"{Fore.GREEN}  ✓ Written {len(key_bytes)} bytes")
            
            # Verify key was saved
            if os.path.exists(ca_key_path):
                file_size = os.path.getsize(ca_key_path)
                print(f"{Fore.GREEN}✓ CA Private Key saved successfully: {ca_key_path} ({file_size} bytes)")
            else:
                print(f"{Fore.RED}✗ Failed to save CA private key!")
            
            return self.ca_cert, self.ca_key
            
        except Exception as e:
            print(f"{Fore.RED}✗ Error creating CA certificate: {e}")
            traceback.print_exc()
            return None, None
    
    def create_self_signed_certificate(self, common_name="example.com"):
        """Create a self-signed X.509 certificate"""
        print(f"\n{Fore.CYAN}Creating self-signed certificate for {common_name}...")
        
        try:
            # Generate private key
            print(f"{Fore.YELLOW}  Generating 2048-bit RSA key...")
            private_key = rsa.generate_private_key(
                public_exponent=65537,
                key_size=2048,
                backend=default_backend()
            )
            print(f"{Fore.GREEN}  ✓ Private key generated")
            
            # Certificate details
            subject = issuer = x509.Name([
                x509.NameAttribute(NameOID.COUNTRY_NAME, "IN"),
                x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "Maharashtra"),
                x509.NameAttribute(NameOID.LOCALITY_NAME, "Mumbai"),
                x509.NameAttribute(NameOID.ORGANIZATION_NAME, "Demo Organization"),
                x509.NameAttribute(NameOID.COMMON_NAME, common_name),
            ])
            
            # Use timezone-aware datetime
            now = datetime.datetime.now(datetime.timezone.utc)
            
            # Create certificate
            print(f"{Fore.YELLOW}  Building self-signed certificate...")
            cert = (
                x509.CertificateBuilder()
                .subject_name(subject)
                .issuer_name(issuer)
                .public_key(private_key.public_key())
                .serial_number(x509.random_serial_number())
                .not_valid_before(now)
                .not_valid_after(now + datetime.timedelta(days=365))
                .add_extension(
                    x509.SubjectAlternativeName([
                        x509.DNSName(common_name),
                        x509.DNSName(f"www.{common_name}"),
                    ]),
                    critical=False,
                )
                .sign(private_key, hashes.SHA256(), backend=default_backend())
            )
            print(f"{Fore.GREEN}  ✓ Certificate created")
            
            # Clean filename (remove dots for safety)
            safe_name = common_name.replace(".", "_")
            
            # Save certificate and key
            cert_path = os.path.join(self.cert_dir, f"{safe_name}_selfsigned.pem")
            key_path = os.path.join(self.cert_dir, f"{safe_name}_private_key.pem")
            
            # Save certificate
            print(f"{Fore.YELLOW}  Saving certificate to {cert_path}...")
            with open(cert_path, "wb") as f:
                cert_bytes = cert.public_bytes(serialization.Encoding.PEM)
                f.write(cert_bytes)
                print(f"{Fore.GREEN}  ✓ Written {len(cert_bytes)} bytes")
            
            # Verify certificate was saved
            if os.path.exists(cert_path):
                file_size = os.path.getsize(cert_path)
                print(f"{Fore.GREEN}✓ Self-signed certificate saved: {cert_path} ({file_size} bytes)")
            else:
                print(f"{Fore.RED}✗ Failed to save certificate!")
            
            # Save private key
            print(f"{Fore.YELLOW}  Saving private key to {key_path}...")
            with open(key_path, "wb") as f:
                key_bytes = private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.TraditionalOpenSSL,
                    encryption_algorithm=serialization.NoEncryption()
                )
                f.write(key_bytes)
                print(f"{Fore.GREEN}  ✓ Written {len(key_bytes)} bytes")
            
            # Verify key was saved
            if os.path.exists(key_path):
                file_size = os.path.getsize(key_path)
                print(f"{Fore.GREEN}✓ Private key saved: {key_path} ({file_size} bytes)")
            else:
                print(f"{Fore.RED}✗ Failed to save private key!")
            
            self.display_certificate_info(cert)
            
            return cert, private_key
            
        except Exception as e:
            print(f"{Fore.RED}✗ Error creating self-signed certificate: {e}")
            traceback.print_exc()
            return None, None
    
    def create_ca_signed_certificate(self, common_name="client.example.com"):
        """Create a certificate signed by CA"""
        if not self.ca_cert or not self.ca_key:
            print(f"{Fore.YELLOW}CA not found, creating one first...")
            self.create_ca_certificate()
        
        print(f"\n{Fore.CYAN}Creating CA-signed certificate for {common_name}...")
        
        try:
            # Generate private key for the certificate
            print(f"{Fore.YELLOW}  Generating 2048-bit RSA key...")
            cert_key = rsa.generate_private_key(
                public_exponent=65537,
                key_size=2048,
                backend=default_backend()
            )
            print(f"{Fore.GREEN}  ✓ Private key generated")
            
            # Certificate details
            subject = x509.Name([
                x509.NameAttribute(NameOID.COUNTRY_NAME, "IN"),
                x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "Karnataka"),
                x509.NameAttribute(NameOID.LOCALITY_NAME, "Bangalore"),
                x509.NameAttribute(NameOID.ORGANIZATION_NAME, "Client Organization"),
                x509.NameAttribute(NameOID.COMMON_NAME, common_name),
            ])
            
            # Use timezone-aware datetime
            now = datetime.datetime.now(datetime.timezone.utc)
            
            # Create certificate signed by CA
            print(f"{Fore.YELLOW}  Building CA-signed certificate...")
            cert = (
                x509.CertificateBuilder()
                .subject_name(subject)
                .issuer_name(self.ca_cert.issuer)
                .public_key(cert_key.public_key())
                .serial_number(x509.random_serial_number())
                .not_valid_before(now)
                .not_valid_after(now + datetime.timedelta(days=365))
                .add_extension(
                    x509.SubjectAlternativeName([
                        x509.DNSName(common_name),
                    ]),
                    critical=False,
                )
                .sign(self.ca_key, hashes.SHA256(), backend=default_backend())
            )
            print(f"{Fore.GREEN}  ✓ Certificate created and signed by CA")
            
            # Clean filename
            safe_name = common_name.replace(".", "_")
            
            # Save certificate and key
            cert_path = os.path.join(self.cert_dir, f"{safe_name}_ca_signed.pem")
            key_path = os.path.join(self.cert_dir, f"{safe_name}_ca_signed_key.pem")
            
            # Save certificate
            print(f"{Fore.YELLOW}  Saving certificate to {cert_path}...")
            with open(cert_path, "wb") as f:
                cert_bytes = cert.public_bytes(serialization.Encoding.PEM)
                f.write(cert_bytes)
                print(f"{Fore.GREEN}  ✓ Written {len(cert_bytes)} bytes")
            
            # Verify certificate was saved
            if os.path.exists(cert_path):
                file_size = os.path.getsize(cert_path)
                print(f"{Fore.GREEN}✓ CA-signed certificate saved: {cert_path} ({file_size} bytes)")
            else:
                print(f"{Fore.RED}✗ Failed to save certificate!")
            
            # Save private key
            print(f"{Fore.YELLOW}  Saving private key to {key_path}...")
            with open(key_path, "wb") as f:
                key_bytes = cert_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.TraditionalOpenSSL,
                    encryption_algorithm=serialization.NoEncryption()
                )
                f.write(key_bytes)
                print(f"{Fore.GREEN}  ✓ Written {len(key_bytes)} bytes")
            
            # Verify key was saved
            if os.path.exists(key_path):
                file_size = os.path.getsize(key_path)
                print(f"{Fore.GREEN}✓ Private key saved: {key_path} ({file_size} bytes)")
            else:
                print(f"{Fore.RED}✗ Failed to save private key!")
            
            self.display_certificate_info(cert)
            
            return cert
            
        except Exception as e:
            print(f"{Fore.RED}✗ Error creating CA-signed certificate: {e}")
            traceback.print_exc()
            return None
    
    def display_certificate_info(self, cert):
        """Display certificate information"""
        print(f"\n{Fore.YELLOW}Certificate Information:")
        print(f"  Serial Number: {cert.serial_number}")
        print(f"  Issuer: {cert.issuer.rfc4514_string()}")
        print(f"  Subject: {cert.subject.rfc4514_string()}")
        print(f"  Valid From: {cert.not_valid_before_utc}")
        print(f"  Valid Until: {cert.not_valid_after_utc}")
        print(f"  Signature Algorithm: {cert.signature_algorithm_oid._name}")
    
    def list_certificates(self):
        """List all certificates in the directory"""
        print(f"\n{Fore.CYAN}=== Certificates in {self.cert_dir} ===")
        
        if os.path.exists(self.cert_dir):
            files = os.listdir(self.cert_dir)
            if files:
                for file in files:
                    file_path = os.path.join(self.cert_dir, file)
                    file_size = os.path.getsize(file_path)
                    print(f"  {Fore.GREEN}✓ {file} ({file_size} bytes)")
            else:
                print(f"  {Fore.YELLOW}No certificates found in directory")
        else:
            print(f"  {Fore.RED}Directory does not exist!")
    
    def explain_pki_components(self):
        """Explain PKI components and trust models"""
        print(f"\n{Fore.CYAN}=== PKI Components and Trust Models ===")
        print(f"""
{Fore.YELLOW}1. CERTIFICATE AUTHORITY (CA):
   • Issues and signs digital certificates
   • Trusted third party
   • Maintains certificate database
   • Root CA → Intermediate CA → End-entity certificates

{Fore.YELLOW}2. CERTIFICATE REVOCATION LIST (CRL):
   • List of revoked certificates
   • Updated periodically by CA
   • Checked during certificate validation
   • Alternative: OCSP (Online Certificate Status Protocol)

{Fore.YELLOW}3. CERTIFICATE CHAIN:
   • Root CA Certificate (self-signed, trusted)
     └─> Intermediate CA Certificate
         └─> End-entity Certificate (website/user)
   • Each level signs the next
   • Verification traces back to trusted root

{Fore.YELLOW}4. TRUST MODELS:

   {Fore.GREEN}a) Hierarchical Trust Model:
      • Single root CA at top
      • Tree structure with subordinate CAs
      • Used in most web browsers

   {Fore.GREEN}b) Web of Trust:
      • No central authority
      • Users sign each other's keys
      • Used in PGP/GPG

   {Fore.GREEN}c) Bridge Trust Model:
      • Multiple PKI domains connected
      • Bridge CA enables cross-certification

{Fore.YELLOW}5. BROWSER HTTPS VALIDATION:
   1. Browser connects to HTTPS site
   2. Server sends certificate chain
   3. Browser verifies:
      • Certificate signature
      • Certificate validity dates
      • Domain name match
      • Not in revocation list
      • Chain leads to trusted root CA
   4. If all checks pass → secure connection established
   5. Otherwise → security warning displayed
        """)

def main():
    print(f"{Style.BRIGHT}{Fore.MAGENTA}=== Q3: Public Key Infrastructure (PKI) ===\n")
    
    if not HAS_COLOR:
        print("Note: Install 'colorama' for colored output: pip install colorama\n")
    
    try:
        pki = PKISimulator()
        
        # Part A: Create self-signed certificate
        print(f"\n{Fore.CYAN}Part A: Self-Signed X.509 Certificate")
        print("="*50)
        pki.create_self_signed_certificate("demo.example.com")
        
        # Create CA and CA-signed certificate
        print(f"\n{Fore.CYAN}Creating Certificate Hierarchy")
        print("="*50)
        pki.create_ca_certificate()
        pki.create_ca_signed_certificate("secure.example.com")
        
        # List all created certificates
        pki.list_certificates()
        
        # Part B & C: Explain PKI components
        print(f"\n{Fore.CYAN}Part B & C: PKI Components and Trust Models")
        print("="*50)
        pki.explain_pki_components()
        
        print(f"\n{Fore.GREEN}✓ Q3 Complete! Check 'certificates' directory for generated files.")
        print(f"{Fore.YELLOW}Full path: {pki.cert_dir}")
        
    except Exception as e:
        print(f"{Fore.RED}✗ Fatal error: {e}")
        traceback.print_exc()
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())