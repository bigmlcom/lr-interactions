# indices of non-zero coefficients
indices = [1,3,5]
predictors = ['type\t\t','citric acid\t','citric acid*type']

def flatten_list(l):
    return [i for sublist in l for i in sublist]

def get_vals(obj,n):
    flat = flatten_list(obj)
    vals = [float(flat[i]) for i in indices[:n]]
    #if n > 1:
    #     vals[0],vals[1] = vals[1],vals[0]
    return [float(flat[-1])] + vals

def print_coeff_table(lr):
    n = len(lr['object']['input_fields'])
    lr = lr['object']['logistic_regression']
    coeffs = get_vals(lr['coefficients'][0][1],n)
    pvals = get_vals(lr['stats'][0][1]['p_values'],n)
    confs = get_vals(lr['stats'][0][1]['confidence_intervals'],n)
    names = ['Intercept\t'] + predictors[:len(coeffs)-1]
    print('\nPredictor\t\t Coefficient\t p-value\t 95% Confidence Interval')
    print('-'*80)
    row_template = '%s\t %0.5f\t %0.5f\t [%0.5f, %0.5f]'
    for n,b,p,c in zip(names,coeffs,pvals,confs):
        print(row_template % (n,b,p,b-c,b+c))
    return (coeffs,pvals,confs)

if __name__ == '__main__':
    from bigml.api import BigML
    from pprint import pprint
    api = BigML()
    lr = api.get_logistic_regression('logisticregression/57f49cce01440448890005aa')
    #pprint(lr)
    print_coeff_table(lr)
    
    lr = api.get_logistic_regression('logisticregression/57f49d5a01440448890005b3')
    cs,ps,confs = print_coeff_table(lr)