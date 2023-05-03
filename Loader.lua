print("sxoware Loader Initialized.")

local Utility = {}

Utility.HTTPRequest = (syn and syn.request) or (http and http.request) or http_request or (fluxus and fluxus.request) or request

if not Utility.Request then
    Utility.Request = function(Table)
        local Response = {}
        Response.Body = game:HttpGet(Table.Url)
        return Response
    end
end

local SupportedGames = {
    8726743209
}

if table.find(SupportedGames, game.PlaceId) then
    print("Loading place-specific script!")
    local Script = Utility.HTTPRequest({Url = "https://raw.githubusercontent.com/centerepic/sxoware/main/" .. tostring(game.PlaceId) .. ".lua"}).Body
    loadstring(Script)()
else
    error("Game is not supported by sxoware. PlaceId - " .. tostring(game.PlaceId))
end