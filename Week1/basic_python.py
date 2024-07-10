import math
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

    precision = tp/(tp+fp)
    recall = tp/(tp+fn)
    f1_score = 2*((precision*recall)/precision+recall)
    print(f'Presion is {precision}')
    print(f'Recall is {recall}')
    print(f'F1-score is {f1_score}')


def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True


def calc_activation_func(x, act_name):
    def calc_relu(x):
        if x <= 0:
            result = 0.0
        else:
            result = x
        return float(result)

    def calc_sig(x):
        return 1./(1+math.e**(-x))

    def calc_elu(x):
        alpha = 0.01
        result = None
        if x < 0:
            result = alpha*(math.e**x - 1)
        else:
            result = x
        return result

    result = None
    if act_name == 'relu':
        result = calc_relu(x)
    elif act_name == 'sigmoid':
        result = calc_sig(x)
    elif act_name == 'elu':
        result = calc_elu(x)
    return result


def exercise2():
    x = input('Input x = ')
    if not is_number(x):
        print('x must be a number')
        return  # exit()

    act_name = input('Input activation Function (sigmoid|relu|elu): ')
    x = float(x)
    result = calc_activation_func(x, act_name)
    if result is None:
        print(f'{act_name} is not supportted')
    else:
        print(f'{act_name}: f({x}) = {result}')


def calc_se(y, y_hat):
    return (y-y_hat)**2


def calc_ae(y, y_hat):
    return abs(y-y_hat)


def calc_se(y, y_hat):
    return (y-y_hat)**2


def exercise3():
    num_samples = input(
        'Input number of samples (integer number) which are generated: ')
    if not num_samples.isnumeric():  # Hàm isnumeric() trong Python trả về true nếu một chuỗi dạng Unicode chỉ chứa các ký tự số,
        # nếu không là false.
        print("number of samples must be an integer number")
        return  # exit()
    loss_name = input('Input loss name: ')


    final_loss = 0
    num_samples = int(num_samples)
    for i in range(num_samples):
        pred_sample = random.uniform(0, 10)
        target_sample = random.uniform(0, 10)

        if loss_name == 'MAE':
            loss = calc_ae(pred_sample, target_sample)
        elif loss_name == 'MSE' or loss_name == 'RMSE':
            loss = calc_se(pred_sample, target_sample)
        # else : catch error
        final_loss += loss
        print(
            f'loss_name: {loss_name}, sample: {i}: pred: {pred_sample} target: {target_sample} loss: {loss}')

    final_loss /= num_samples
    if loss_name == 'RMSE':
        final_loss = math.sqrt(final_loss)
    print(f'final {loss_name}: {final_loss}')


def approx_sin(x, n):
    res = 0
    for i in range(n):
        res += (-1)**i*(x**(2*i+1))/math.factorial(2*i+1)
    return res


def approx_cos(x, n):
    res = 0
    for i in range(n):
        res += (-1)**i*(x**(2*i))/math.factorial(2*i)
    return res


def approx_sinh(x, n):
    res = 0
    for i in range(n):
        res += (x**(2*i+1))/math.factorial(2*i+1)
    return res


def approx_cosh(x, n):
    res = 0
    for i in range(n):
        res += x**(2*i)/math.factorial(2*i)
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
    exercise2()
    # Bài 3:
    exercise3()
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
