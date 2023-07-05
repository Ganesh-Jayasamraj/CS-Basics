# Variables
students_name = "Ram"
roll_no = 15
maths_mark = 9.0

# Array
arr = [1, 2, 3, 4, 5]

# Uninitialinzed Array
array = Array{Int64}(undef, 3)

array = Array{Int64}(undef, 3, 3, 3)

arr = [1, 2, 3]

new_array = [1, "text", 7.4, tan, pi]

pi

[1 2 3 4 5 6 7 8 9 10]

[1 2 3 4 5 ; 6 7 8 9 10]

collect(1:5)

collect(1.5:5.5)

collect(0: 5: 50)

# Ellipsis / splat operator

[0:10...]

range(1, length = 15, stop = 150)

collect(range(1, length=15, stop=150))

[n^2 for n in 1:100]

collect(n^2 for n in 1:100)

[n*m for n in 1:10, m in 1:15]

zeros(Int64, 4, 5)

ones(Float64, 4, 5)

rand(Float64, 4, 5)

rand(Int64, 4, 5)