# Define the Azure DevOps organization name
$organization = 

# Define the Azure DevOps project name
$project = 

# Define the Azure DevOps repository ID or name
$repoId = 

# Define the path to the file in the repository
$path = 

# Define the Personal Access Token (PAT) for authentication
$personalAccessToken = 

# Encode the Personal Access Token in Base64 format for Basic Authentication
$encodedAuth = [Convert]::ToBase64String([Text.Encoding]::ASCII.GetBytes(":$personalAccessToken"))

# Create an authentication header for the API request
$headers = @{ Authorization = "Basic $encodedAuth" }

# Construct the API URL to fetch repository details (to be filled in)
$url = 

# Print the API request URL to the console for debugging
Write-Host "Testing API Request: $url"

# Send an API request using Invoke-RestMethod to fetch repository details
$response = Invoke-RestMethod -Uri $url -Headers $headers -Method Get

# Print the API response in JSON format
Write-Host "API Response:"
$response | ConvertTo-Json -Depth 3

# Define the API URL to fetch file content from the repository (to be filled in)
$fileUrl = 

# Fetch the file content from the given URL
$response = Invoke-RestMethod -Uri $fileUrl -Headers $headers -Method Get

# Print the first 500 characters of the file content
Write-Host "File Content (/Sandbox/app.py):"

# Check if the API response contains the `content` field
Write-Host "Checking if `content` exists..."
if ($response.PSObject.Properties.Name -contains "content") {
    # If `content` exists, print confirmation and the first 500 characters of the file
    Write-Host " File content exists!"
    Write-Host $response.content.Substring(0, 500)
} else {
    # If `content` is missing, notify the user
    Write-Host " `content` is missing from the response!"
}

# Print the full API response in JSON format for debugging
Write-Host "Raw API Response:"
Write-Host $response | ConvertTo-Json -Depth 10
