# Import the Active Directory module

# Script: Ops 301 challenge 13
# Authur: Will B. with the help of ChatGPT
# Date: 12/13/2023

Import-Module ActiveDirectory

# Define user attributes
$firstName = "Franz"
$lastName = "Ferdinand"
$username = "ferdi"
$office = "Springfield, OR"
$department = "TPS Department"
$email = "ferdi@GlobeXpower.com"
$jobTitle = "TPS Reporting Lead"

# Set the password for the new user
$password = ConvertTo-SecureString "P@ssw0rd" -AsPlainText -Force

# Specify the OU (Organizational Unit) where the user will be created
$ou = "OU=Users,DC=YourDomain,DC=com"

# Create the new user, This script below that is commented out doesn't specifically work but has the instructions 
# New-ADUser -SamAccountName $username -UserPrincipalName "$username@YourDomain.com" -Name "$firstName $lastName" -GivenName $firstName -Surname $lastName -EmailAddress $email -Office $office -Title $jobTitle -Department $department -Enabled $true -AccountPassword $password -Path $ou