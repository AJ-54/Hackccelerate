--[[
*****************************************************************************************
*
*
*  This script is code stub for CodeChef problem code INV_LUA
*  under contest PYLT20TS in Task 0 of Nirikshak Bot (NB) Theme (eYRC 2020-21).
*
*  Filename:            INV_LUA.lua
*  Created:             07/10/2020
*  Last Modified:       07/10/2020
*  Author:              e-Yantra Team
*
*****************************************************************************************
]]--
 
-- manageInventory function to add, update / delete items to / from the Inventory

function mysplit (inputstr, sep)
        if sep == nil then
                sep = "%s"
        end
        local t={}
        for str in string.gmatch(inputstr, "([^"..sep.."]+)") do
                table.insert(t, str)
        end
        return t
end

function manageInventory()
	-- reading total Items N
	local m = {}
	local t= {}
	local sum = 0
	N = tonumber(io.read())
	for i=1,N 
	do
		t=mysplit(io.read()," ")
		m[t[1]]=tonumber(t[2])
		sum=sum+tonumber(t[2])
	end
		
 
    -- write your code here
 
    -- reading total M operations to perform
	M = tonumber(io.read())
	
	for i =1,M
	do
		t=mysplit(io.read()," ")
		if t[1] == "ADD" then 
			if m[t[2]]  == nil then
				m[t[2]] =tonumber(t[3])
				io.write("ADDED Item ")
				io.write(t[2])
				io.write("\n")
				sum=sum+tonumber(t[3])
			else
			    sum = sum + t[3] - m[t[2]]
				m[t[2]]=m[t[2]]+tonumber(t[3])
				io.write("UPDATED Item ")
				io.write(t[2])
				io.write("\n")
			end
		else
			if m[t[2]]  == nil then
				io.write("Item ")
				io.write(t[2])
				io.write(" does not exist\n")
			else
				if m[t[2]] <tonumber(t[3]) then
					io.write("Item ")
				    io.write(t[2])
				    io.write(" could not be DELETED\n")
				else 
				   m[t[2]]=m[t[2]]-tonumber(t[3])
				   io.write("DELETED Item ")
				   io.write(t[2])
				   sum=sum-tonumber(t[3])
				   io.write("\n")
				end
			end
		end
	end


 
    -- write your code here
 
    -- calculate the sum of items
    
 
    -- write your code here    
 
    print(sum)
end
 
-- for each case, call the manageInventory function to add, update / delete items to / from the Inventory
tc = tonumber(io.read())
i = 0
while i < tc do
    manageInventory()
    i = i + 1
end
 