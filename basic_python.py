from math import *
import random


def classification(tp, fp, fn):
    if not isinstance(tp, int):
        print('tp must be int')
        return
    if not isinstance(fp, int):
        print('fp must be int')
        return

    if not isinstance(fn, int):
        print('fn must be int')
        return

    if tp <= 0 or fp <= 0 or fn <= 0:
        print('tp and fn and fn must be greater than zero')
        return

    Precision = tp/(tp+fp)
    Recall = tp/(tp+fn)
    F1_score = 2*((Precision*Recall)/Precision+Recall)
    print(f'Presion is {Precision}')
    print(f'Recall is {Recall}')
    print(f'F1-score is {F1_score}')


def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True


def activation():
    x = input('Input x = ')
    if is_number(x) == False:
        print('x must be a number')
    else:
        activation = input('Input activation Function (sigmoid|relu|elu): ')

        if activation != 'sigmoid' and activation != 'relu' and activation != 'elu':
            print(f'{activation} is not supportted')
        if activation == 'sigmoid':
            sigmoid = 1/(1+e**(-float(x)))
            print(f'f({x}) = {sigmoid}')
        elif activation == 'relu':
            if x <= 0:
                print(0)
            else:
                print(f'relu({x}) = {x}')
        elif activation == 'elu':
            if x <= 0:
                print(f'ELU({x}) = {0.01*(e**float(x)-1)}')
            else:
                print(f'ELU({x}) = {x}')


def regression_selection():
    num_samples = input(
        'Input number of samples (integer number) which are generated: ')
    if not num_samples.isnumeric():
        print('number of samples must be an integer number')
        return
    else:
        num_samples = int(num_samples)
        lossname = input('Input loss name: ')
        target = [random.uniform(0, 10) for i in range(num_samples)]
        predict = [random.uniform(0, 10) for i in range(num_samples)]
        loss = 0
        mae, mse, rmse = 0, 0, 0
        for i in range(num_samples):
            if lossname == 'MAE':
                mae += abs(target[i]-predict[i])
                print(
                    f'lossname: {lossname} , sample: {i} , pred: {predict[i]}, target: {target[i]} , loss: {mae}')
            if lossname == 'MSE':
                mse += (target[i]-predict[i])**2
                print(
                    f'lossname: {lossname} , sample: {i} , pred: {predict[i]}, target: {target[i]} , loss: {mse}')
            if lossname == 'RMSE':
                rmse += (target[i]-predict[i])**2
                print(
                    f'lossname: {lossname} , sample: {i} , pred: {predict[i]}, target: {target[i]} , loss: {rmse}')
        if lossname == 'MAE' or lossname == 'MSE':
            loss = (1/num_samples)*(mae+mse)
            print(f'final {lossname}: {loss}')
        elif lossname == 'RMSE':
            loss = sqrt((1/num_samples)*rmse)
            print(f'final {lossname}: {loss}')


def approx_sin(x, n):
    res = 0
    for i in range(n):
        res += (-1)**i*(x**(2*i+1))/factorial(2*i+1)
    return res


def approx_cos(x, n):
    res = 0
    for i in range(n):
        res += (-1)**i*(x**(2*i))/factorial(2*i)
    return res


def approx_sinh(x, n):
    res = 0
    for i in range(n):
        res += (x**(2*i+1))/factorial(2*i+1)
    return res


def approx_cosh(x, n):
    res = 0
    for i in range(n):
        res += x**(2*i)/factorial(2*i)
    return res


def md_nre_single_sample(y, y_hat, n, p):
    md_nre = (y**(1/n)-y_hat**(1/n))**p
    return md_nre


if __name__ == '__main__':
    # Bài 1:
    classification(tp=2, fp=3, fn=4)
    classification(tp='a', fp=3, fn=4)
    classification(tp=2, fp='a', fn=4)
    classification(tp=2, fp=3, fn='a')
    classification(tp=2, fp=3, fn=0)
    classification(tp=2.1, fp=3, fn=0)
    # Bài 2:
    activation()
    # Bài 3:
    regression_selection()
    # Bài 4:
    print(approx_sin(x=3.14, n=10))
    print(approx_cos(x=3.14, n=10))
    print(approx_sinh(x=3.14, n=10))
    print(approx_cosh(x=3.14, n=10))
    # Bài 5:
    print(md_nre_single_sample(y=100, y_hat=99.5, n=2, p=1))
    print(md_nre_single_sample(y=50, y_hat=49.5, n=2, p=1))
    print(md_nre_single_sample(y=20, y_hat=19.5, n=2, p=1))
    print(md_nre_single_sample(y=0.6, y_hat=0.1, n=2, p=1))
