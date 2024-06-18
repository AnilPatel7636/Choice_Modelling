import numpy as np

def calculate_probabilities(parameters,data,utilities):
    # calculating utilities for each alternative by calling functions V1, V2 & V3
    V = [utility(parameters, data) for utility in utilities]

    # initialize dictionaries to store probabilities and output
    output = {}
    # probabilities dict. is basically storing P1,P2,P3 as three keys and their values are a list containing probability of each alternative.
    probabilities= {}

    # calculating probabilities P1,P2 & P3 for each alternative
    # iterating through each alternative's deterministic utility (Vi) and its index (i)
    for i,Vi in enumerate(V):

        num = data[f'AV{i+1}'] * np.exp(Vi)
        den = sum(data[f'AV{j+1}'] * np.exp(Vj) for j,Vj in enumerate(V))

        # calculating probability for the current alternative
        probabilities[f'P{i+1}'] = num/den

    # set values as required in output according to question in output dict.
    for i in range(len(data['X1'])):
        l=[]
        for j in probabilities:
            l.append(probabilities[j][i])
        output[i]=l

    # save probabilities to a .txt file
    file = open('output.txt', 'w')
    for key, value in output.items():
        file.write(f'{key}: {value}\n')
    file.close()
    return output

# functions to calculate the utility for each alternative
# function Vi's (i=1,2,3) returns a array as we are using numpy here (np.array(data[])), that gives an array of size same as of attributes
# then we are computing further calculations with that array to get required probalities for each alternative
def V1(parameters, data):
    return parameters['β01'] + parameters['β1']*np.array(data['X1']) + parameters['βS1,13']*np.array(data['S1'])

def V2(parameters, data):
    return parameters['β02'] + parameters['β2']*np.array(data['X2']) + parameters['βS1,23']*np.array(data['S1'])

def V3(parameters, data):
    return parameters['β03'] + parameters['β1']*np.array(data['Sero']) + parameters['β2']*np.array(data['Sero'])

# given parameters & data
parameters = {'β01': 0.1, 'β1': -0.5, 'β2': -0.4, 'β02': 1, 'β03': 0, 'βS1,13': 0.33, 'βS1,23': 0.58}
data = {
    'X1': [2,1,3,4,2,1,8,7,3,2],
    'X2': [8,7,4,1,4,7,2,2,3,1],
    'Sero': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'S1': [3,8,4,7,1,6,5,9,2,3],
    'AV1' : [1,1,1,1,1,0,0,1,1,0],
    'AV2': [1,1,1,0,0,1,1,1,0,1],
    'AV3': [1,1,0,0,1,1,1,1,1,1]
}

try:
    # trying function calling and printing final output if there are no errors
    result = calculate_probabilities(parameters, data, [V1, V2, V3])
    print(result)

except ValueError as e:
    # raise an exception in case of an error for size mismatch(here).
    print(f"input error:{e} \n size of alternatives mismatch in attributes of data!")