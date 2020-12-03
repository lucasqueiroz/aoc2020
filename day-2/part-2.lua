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
    first, second, char, password = string.match(line, "(%d+)-(%d+) (%a+): (%a+)")
    first_char = string.sub(password, first, first)
    second_char = string.sub(password, second, second)
    if (
        (first_char == char) and not (second_char == char) or
        (second_char == char) and not (first_char == char)
    ) then
        valid = valid + 1
    end
end

print(valid)
