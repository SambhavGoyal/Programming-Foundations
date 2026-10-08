# Note that these collections can be mutable (list) or immutable (tuples)

# # Nearest stars to Earth
# star1 = 'Sol'
# star2 = 'Alpha Centauri'
# star3 = 'Barnard'
# star4 = 'Wolf 359'

stars = ['Sol',
         'Alpha Centauri',
         'Barnard',
         'Wolf 359']

print("The third star is", stars[2])

# Highest peak on each tectonic plate
African = 'Kilimanjaro'
Antarctic = 'Vinson'
Australian = 'Puncak Jaya'
Eurasian = 'Everest'
North_American = 'Denali'
Pacific = 'Mauna Kea'
South_American = 'Aconcagua'

peaks = {
    'African' : 'Kilimanjaro',
    'Antarctic' : 'Vinson',
    'Australian' : 'Puncak Jaya',
    'Eurasian' : 'Everest',
    'North_American' : 'Denali',
    'Pacific' : 'Mauna Kea',
    'South_American' : 'Aconcagua'
}

print("Highest peak on Pacific plate is", peaks['Pacific'])