# Function to create a list of integers from user input
function Get-IntegerList {
  param()

  $numbers = @()
  while ($true) {
    $userInput = Read-Host "Enter an integer (or press Enter to finish): "
    if ($userInput -eq "") {
      break
    }
    $number = 0
    if ([int]::TryParse($userInput, [ref] $number)) {
      $numbers += $number
    } else {
      Write-Warning "Invalid input. Please enter an integer."
    }
  }
  return $numbers
}

# Get the list of integers from the user
$numbers = Get-IntegerList

# Check if any numbers were entered
if ($numbers.Count -eq 0) {
  Write-Host "No integers were entered."
  exit
}

# Print all elements in the list
Write-Host "Elements in the list:"
$numbers | ForEach-Object { Write-Host $_ }

# Find the sum of all elements
$sum = $numbers | Measure-Object -Sum | Select-Object -ExpandProperty Sum

# Find the maximum and minimum elements
$max = $numbers | Measure-Object -Maximum | Select-Object -ExpandProperty Maximum
$min = $numbers | Measure-Object -Minimum | Select-Object -ExpandProperty Minimum

Write-Host "Sum of all elements: $sum"
Write-Host "Maximum element: $max"
Write-Host "Minimum element: $min"
