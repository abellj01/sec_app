'''
Created on 30 Sep 2019

@author: aymar

'''
print("         Welcome to Geo Cyber Sec Assessment - Protect Your Business\n")

industry = input("Select your industry (Defense /Finance /Public Sector /Charity /Online_Services /Other): ")

if industry == "Defense" or industry == "D" :
    print("\nSummary")
    print("    Sorry, this feature has not been implemented yet.")
    print("    What Next")
    print("    We recommend...read from the following DEFENSE text file.\n")
    print("    It is worth knowing that the Ministry of Defence mandated Cyber Essentials")
    print("    for all its new suppliers and also their relevant supply chain")
elif industry == "Finance" or industry == "F" :
    print("\nSummary")
    print("    Sorry, this feature has not been implemented yet.")
    print("    What Next")
    print("    We recommend...read from the following FINANCE text file.")
elif industry == "Public Sector" or industry == "P" :
    print("\nSummary")
    print("    Sorry, this feature has not been implemented yet.")
    print("    What Next")
    print("    We recommend...read from the following PUBLIC SECTOR text file.\n")
    print("    The UK Government Department of Health, National Data Guardian (NDG) published 'Review of data security, consent \n    and opt-outs' which recommended All health and social care organisations should provide evidence \n    that they are taking action to improve cyber security, for example through the ‘Cyber Essentials’ scheme.")
elif industry == "Charity" or industry == "C" :
    print("\nSummary")
    print("    Sorry, this feature has not been implemented yet.")
    print("    What Next")
    print("    We recommend...read from the following CHARITY text file.")
elif industry == "Online_Services" :
    print("\nSummary")
    print("    This is what will be implemented")
else:
    print("\nSummary")
    print("    Sorry, your industry is not listed")
    print("    What Next:\n    We recommend reading the contents of 'other' text file because:")
    f = open("other.txt", "r")
    print(f.read())
    f.close()