-- Require github scripts.

getgenv().gitquire = function(user : string, repo : string, branch : string, path : string)
    local url = ("https://raw.githubusercontent.com/%s/%s/%s/%s"):format(user, repo, branch, path)
    return loadstring(game:HttpGet(url))()
end
