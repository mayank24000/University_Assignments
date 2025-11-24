#!/usr/bin/env python3
import sys
from certificate_analyzer import SSLAnalyzer
from utils import *

def display_certificate_info(analyzer):
    """Display all certificate information"""
    
    # Basic Information
    print_section("BASIC CERTIFICATE INFORMATION")
    basic_info = analyzer.get_basic_info()
    if basic_info:
        print_info("Common Name (CN)", basic_info['subject'].get('commonName', 'N/A'))
        print_info("Organization (O)", basic_info['subject'].get('organizationName', 'N/A'))
        print_info("Country (C)", basic_info['subject'].get('countryName', 'N/A'))
        print_info("Serial Number", basic_info.get('serial_number', 'N/A'))
    
    # Issuer Information
    print_section("CERTIFICATE ISSUER (CA)")
    if basic_info:
        print_info("Issuer CN", basic_info['issuer'].get('commonName', 'N/A'))
        print_info("Issuer Organization", basic_info['issuer'].get('organizationName', 'N/A'))
        print_info("Issuer Country", basic_info['issuer'].get('countryName', 'N/A'))
    
    # Validity Information
    print_section("VALIDITY PERIOD")
    validity = analyzer.get_validity_info()
    if validity:
        print_info("Valid From", validity['not_before'])
        print_info("Valid Until", validity['not_after'])
        
        status_color = Fore.GREEN if validity['is_valid'] else Fore.RED
        status_text = "✅ VALID" if validity['is_valid'] else "❌ INVALID/EXPIRED"
        print_info("Status", status_text, status_color)
        
        if not validity['expired']:
            expire_color = Fore.GREEN if validity['days_to_expire'] > 30 else Fore.RED
            print_info("Days Until Expiry", str(validity['days_to_expire']), expire_color)
    
    # Subject Alternative Names
    print_section("SUBJECT ALTERNATIVE NAMES (SANs)")
    sans = analyzer.get_subject_alternative_names()
    if sans:
        print_list(sans[:10])  # Show first 10
        if len(sans) > 10:
            print(f"  ... and {len(sans) - 10} more")
    else:
        print("  No SANs found")
    
    # Public Key Information
    print_section("PUBLIC KEY INFORMATION")
    pub_key = analyzer.get_public_key_info()
    if pub_key:
        print_info("Algorithm", pub_key.get('type', 'N/A'))
        if pub_key.get('size'):
            print_info("Key Size", f"{pub_key['size']} bits")
    
    # Signature Algorithm
    print_section("SIGNATURE ALGORITHM")
    sig_algo = analyzer.get_signature_algorithm()
    print_info("Algorithm", sig_algo or 'N/A')
    
    # Security Analysis
    print_section("SECURITY ANALYSIS")
    security_issues = analyzer.analyze_security()
    print_list(security_issues)

def main():
    """Main application entry point"""
    print_header("SSL/TLS CERTIFICATE ANALYZER")
    
    # Get hostname from user
    if len(sys.argv) > 1:
        hostname = sys.argv[1]
    else:
        hostname = input("Enter website URL or hostname: ").strip()
    
    if not hostname:
        print("❌ No hostname provided!")
        return
    
    # Validate and clean hostname
    hostname = validate_hostname(hostname)
    
    print(f"\n🔍 Analyzing: {Fore.CYAN}{hostname}{Style.RESET_ALL}\n")
    
    # Create analyzer and fetch certificate
    analyzer = SSLAnalyzer(hostname)
    
    if analyzer.get_certificate():
        display_certificate_info(analyzer)
        print_header("ANALYSIS COMPLETE")
    else:
        print("\n❌ Failed to retrieve certificate\n")

if __name__ == "__main__":
    main()