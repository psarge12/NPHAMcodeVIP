import numpy as np

vals = np.array([[-0.012,-0.175,-0.126,0.048,-0.033],
                 [-0.001,0.001,-0.044,0.0,0.0],
                 [0.0,0.0,-0.005,0.0,0.011],
                 [0.0,0.0,-0.031,0.0,-0.015],
                 [-0.004,-0.043,-0.041,0.001,-0.032],
                 [0.0,0.0,0.0,0.005,0.0],
                 [-0.003,-0.044,-0.024,0.0,0.0],
                 [-0.258,-3.013,-2.735,-0.215,0.0],
                 [0.007,0.087,0.088,0.0,-0.049],
                 [0.0,0.0,0.0,0.0,-0.009],
                 [-0.007,0.0,-0.131,-0.043,0.126],
                 [0.0,0.0,0.0,0.0,0.0],
                 [0.0,-0.037,-0.034,0.005,0.0],
                 [-0.001,-0.011,-0.002,0.011,-0.026],
                 [0.0,0.0,0.0,0.016,0.0],
                 [0.0,0.0,0.0,0.0,0.204],
                 [0.0,0.0,0.0,0.0,0.0],
                 [-0.001,0.0,0.0,0.0,0.005],
                 [0.001,-0.051,0.003,0.359,0.231],
                 [-0.047,-0.652,-0.151,0.080,-0.166],
                 [0.013,0.208,0.071,-0.212,-0.294],
                 [-0.021,-0.087,-0.435,-0.909,0.181],
                 [0.005,0.074,0.026,-0.139,-0.933],
                 [-0.003,-0.056,0.023,0.284,0.591],
                 [-0.024,-0.278,-0.352,-0.221,-0.617],
                 [0.042,0.514,0.426,0.233,1.014],
                 [0.007, 0.098, 0.136, 0.107, 0.399],
                 [0.017,0.155,0.236, 0.089, 0.016],
                 [4.191,10.028,8.395,-0.423,-2.513],
                 [0.0619,0.0422,0.0345,0.0501,0.1713]])

inp = np.array([[0.0],   #population denisyt
                [0.0],       #employment denisty 
                [0.092],   #job accessibility by transit  https://www.economyleague.org/resources/greater-philadelphias-public-transportation-and-covid-19-part-2#:~:text=As%20we%20noted%20last%20week,public%20transit%20commuters%20%5B1%5D.
                [0.135],   # percent developed open space   https://whyy.org/articles/what-percentage-of-philly-s-land-area-do-the-different-zoning-categories-cover/#:~:text=Parks%20and%20open%20space%20cover,of%20Philly's%20zoned%20land%20area.
                [0.2],   # tree canopy   https://phillytrees.azavea.com/#:~:text=As%20of%202018%2C%20trees%20covered,6%25%20of%20its%20tree%20coverage.
                [0.8],   # employment entropy    https://www.transportation.gov/mission/health/land-use-mix#:~:text=The%20employment%20entropy%20variable%20from,a%200%20to%201%20scale.
                [0],   # Trip equilibirum    https://www.jstor.org/stable/25767845   Not good data being found
                [0.54],   # percent of population working age    https://philaworks.org/philadelphias-population/#:~:text=About%2054%20percent%20of%20residents,percent%2C%20are%2065%20and%20older.
                [0.33],   #percent zero vehicle households    https://www.phillymag.com/citified/2015/03/03/philly-is-one-most-car-free-cities-us/
                [.041],   # total retail employment in CBG   https://centercityphila.org/uploads/attachments/cj1hzfjxw090c10qdnbrxawt3-17-socc-employment.pdf
                [.012],   # total population in CBG   https://en.wikipedia.org/wiki/Center_City,_Philadelphia
                [0.12],   # percent forest land cover    https://www.globalforestwatch.org/dashboards/country/USA/39/51/?category=forest-change&map=eyJjZW50ZXIiOnsibGF0Ijo1My4zODMzMjgzNjc1NzY2NzQsImxuZyI6LTExNi42MzA4NTkzNzUwMjI0fSwiY2FuQm91bmQiOnRydWUsImRhdGFzZXRzIjpbeyJkYXRhc2V0IjoicG9saXRpY2FsLWJvdW5kYXJpZXMiLCJsYXllcnMiOlsiZGlzcHV0ZWQtcG9saXRpY2FsLWJvdW5kYXJpZXMiLCJwb2xpdGljYWwtYm91bmRhcmllcyJdLCJib3VuZGFyeSI6dHJ1ZSwib3BhY2l0eSI6MSwidmlzaWJpbGl0eSI6dHJ1ZX0seyJkYXRhc2V0IjoidHJlZS1jb3Zlci1sb3NzIiwibGF5ZXJzIjpbInRyZWUtY292ZXItbG9zcyJdLCJvcGFjaXR5IjoxLCJ2aXNpYmlsaXR5Ijp0cnVlLCJwYXJhbXMiOnsidGhyZXNob2xkIjo1MCwidmlzaWJpbGl0eSI6dHJ1ZX19XX0%3D&treeLoss=eyJ0aHJlc2hvbGQiOjUwfQ%3D%3D#:~:text=Philadelphia%2C%20Pennsylvania%2C%20United%20States%20Deforestation%20Rates%20%26%20Statistics%20%7C%20GFW&text=In%202010%2C%20Philadelphia%20had%204.38,10.4%20kt%20of%20CO%E2%82%82%20emissions.
                [0.44],   #percent of jobs near fixed transit    https://www.pewtrusts.org/en/research-and-analysis/reports/2019/07/24/the-cost-of-commuting-for-philadelphians
                [0.0],   #percent natural open space
                [0.135],   #Percent natural/devloped open space
                [0.0],   #no transit/GTFS data
                [0.0],   #Network denisty  
                [.07],   #intersection denisty    https://catalog.data.gov/dataset/enviroatlas-philadelphia-pa-estimated-intersection-density-of-walkable-roads1
                [0.48],   #Home renter (vs owner)    https://www.rentcafe.com/average-rent-market-trends/us/pa/philadelphia/#:~:text=Philadelphia%2C%20PA%20Occupied%20Housing%20Units,52%25%20are%20owner%2Doccupied.
                [0.46],   #generder is female (vs male)    https://www.google.com/search?q=gender+breakdown+in+philadelphia&rlz=1C1ONGR_enUS964US964&oq=gender+breakdown+in+philadelphia&gs_lcrp=EgZjaHJvbWUyCQgAEEUYORigATIHCAEQIRigATIHCAIQIRigATIHCAMQIRigATIKCAQQIRgWGB0YHtIBCDQ5MDVqMWo3qAIAsAIA&sourceid=chrome&ie=UTF-8
                [0.962],   # employed (vs not employed)    https://ycharts.com/indicators/philadelphia_pa_unemployment_rate_md#:~:text=Philadelphia%2C%20PA%20Unemployment%20Rate%20(I%3APPAUR)&text=Philadelphia%2C%20PA%20Unemployment%20Rate%20is,long%20term%20average%20of%206.14%25.
                [0.12],   #age 65+ (vs 18-64)   https://sarahralstonfoundation.org/index.php/statistics-on-philadelphias-elderly-population/#:~:text=There%20are%201.6%20M%20people,23%25%20are%2075%20and%20older
                [0.338],   #white non hispanic   https://www.economyleague.org/resources/philadelphia-neighborhood-changes-part-2-race-and-ethnicity
                [0.22],   #low income (vs middle income)   https://www.inquirer.com/news/philadelphia-poverty-rate-big-city-20230914.html#:~:text=Philadelphia's%20poverty%20rate%20has%20been,a%20percentage%20point%20from%202021.
                [0.19],   #high income (vs middle income)   https://statisticalatlas.com/metro-area/Pennsylvania/Philadelphia/Household-Income
                [0.174],   # no hs degree (vs 4 eyar college)    https://www.achieve-now.com/poverty-cycle#:~:text=17.4%25%20of%20adult%20Philadelphians%E2%80%94an,6%25%20behind%20the%20national%20average.
                [0.55],   # hs degree only (vs 4 eyar college)   https://www.achieve-now.com/poverty-cycle#:~:text=17.4%25%20of%20adult%20Philadelphians%E2%80%94an,6%25%20behind%20the%20national%20average.
                [0.12],   # 2 year college (vs 4 year college)  https://www.achieve-now.com/poverty-cycle#:~:text=17.4%25%20of%20adult%20Philadelphians%E2%80%94an,6%25%20behind%20the%20national%20average.
                [.5],   # Intercept
                [.01]])      # mcfaddens pseudo K
            
bmi=0
overweight = 0
obese = 0
mentalhealth = 0
generalhealth=0
i=0
n=0
for each in vals:
    bmi = bmi + (each[i]*inp[n])
    i+=1
    overweight = overweight + (each[i]*inp[n])
    i+=1
    obese = obese + (each[i]*inp[n])
    i+=1
    mentalhealth = mentalhealth + (each[i]*inp[n])
    i+=1
    generalhealth = generalhealth + (each[i]*inp[n])
    i=0
    n+=1

print("BMI Value =", bmi)
print("Percent overweight =", overweight)
print("percent obese =", obese)
print("mental health keppler-6 indicator =", mentalhealth)
print("percent poor health =", generalhealth)