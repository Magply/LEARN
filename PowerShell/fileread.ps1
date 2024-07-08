# Function to count the number of words in a text file
function Get-WordCount {
    param (
        [string]$filePath
    )

    try {
        # Read the content of the file
        $content = Get-Content -Path $filePath -Raw
        # Split the content into words using whitespace as delimiter
        $words = $content -split "\s+"
        # Count the number of words
        $wordCount = $words.Count
        return $wordCount
    } catch {
        Write-Host "An error occurred: $_"
        return $null
    }
}

# Main script
# Prompt the user to enter the file path
$filePath = Read-Host "Enter the path of the text file"

# Get the word count using the function
$wordCount = Get-WordCount -filePath $filePath

# Check if word count was successfully calculated
if ($wordCount -ne $null) {
    Write-Host "The number of words in the file is: $wordCount"
}
