#Run this file in colab as mentioned

#JohntheRipper
#run this in cell block 1 
!apt-get install -y john 

#run these two line in cell block 2
!wget -q https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt -O /tmp/rockyou.txt
print("Downloaded!") 

#Run this in the next cell
import subprocess, hashlib, os

def check_strength_with_john(password):
    # Generate hash
    import subprocess
    h = subprocess.run(['openssl', 'passwd', '-1', password], 
                      capture_output=True, text=True).stdout.strip()
    
    # Write hash file
    with open('/tmp/strength_test.txt', 'w') as f:
        f.write(f'testuser:{h}\n')
    
    # Try to crack it
    os.system('john --wordlist=/tmp/rockyou.txt /tmp/strength_test.txt > /dev/null 2>&1')
    
    result = subprocess.run(['john', '--show', '/tmp/strength_test.txt'], 
                           capture_output=True, text=True).stdout
    
    print(f"\nPassword: {password}")
    if "1 password hash cracked" in result:
        print("WEAK — John cracked it instantly!")
    else:
        print("STRONG — John could not crack it!")

# Test passwords
for pwd in ["123456", "password", "Hello123", "H3ll0@W0rld#99"]:
    check_strength_with_john(pwd)
