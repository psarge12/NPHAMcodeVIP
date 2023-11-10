import numpy as np

vals = np.array([[0.0,0.0,-0.005,0.0,0.011],
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

inp = np.array([[0],   #job accessibility by transit
                [0.4],   # percent developed open space
                [0],   # tree canopy
                [0.6],   # employment entropy
                [0],   # Trip equilibirum
                [0],   # percent of population working age
                [0.23],   #percent zero vehicle households
                [0],   # total retail employment in CBG
                [0],   # total population in CBG
                [0],   # percent forest land cover
                [0],   #percent of jobs near fixed transit
                [0],   #percent natural open space
                [0],   #Percent natural/devloped open space
                [0],   #no transit/GTFS data
                [0],   #Network denisty
                [0],   #intersection denisty
                [0],   #Home renter (vs owner)
                [0],   #generder is female (vs male)
                [0],   # employed (vs not employed)
                [0.4],   #age 65+ (vs 18-64)
                [0],   #white non hispanic
                [0],   #low income (vs middle income)
                [0],   #high income (vs middle income)
                [0],   # no hs degree (vs 4 eyar college)
                [0],   # hs degree only (vs 4 eyar college)
                [0],   # 2 year college (vs 4 year college)
                [0],   # Intercept
                [0]])      # mcfaddens pseudo K
            
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