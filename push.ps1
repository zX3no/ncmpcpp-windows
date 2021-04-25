$Commit = Read-Host -Prompt 'Enter your commit message'
$dir = Get-Location
$confirmation = Read-Host "Are you sure you want to proceed (y/n)"
if ($confirmation -eq 'y') {
    cd $dir
	git checkout main
	git add .
	git commit -am "$Commit"
	git push origin main
}