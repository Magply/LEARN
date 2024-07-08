# Function to reverse a string
function Reverse-String {
    param (
        [string]$inputString
    )
    
    # Convert the string to a character array
    $charArray = $inputString.ToCharArray()
    # Reverse the character array
    [array]::Reverse($charArray)
    # Join the reversed character array back into a string
    $reversedString = -join $charArray
    return $reversedString
}

# Main script
# Prompt the user to enter a string
$userInput = Read-Host "Enter a string"

# Reverse the string using the function
$reversedString = Reverse-String -inputString $userInput

# Print the reversed string
Write-Host "Reversed string: $reversedString"
