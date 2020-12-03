local open = io.open

local function read_file(path)
    local file = open(path, "rb")
    if not file then return nil end
    local lines = file:lines()
    return lines
end

local file_content = read_file("day-2/input");

local valid = 0

for line in file_content do
    min, max, char, password = string.match(line, "(%d+)-(%d+) (%a+): (%a+)")
    _, count = string.gsub(password, char, "")
    if (count >= tonumber(min) and count <= tonumber(max)) then
        valid = valid + 1
    end
end

print(valid)
