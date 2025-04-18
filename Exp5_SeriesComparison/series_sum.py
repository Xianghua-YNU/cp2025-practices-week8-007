import numpy as np
import matplotlib.pyplot as plt

def sum_S1(N):
    """计算第一种形式的级数和：交错级数
    S_N^(1) = sum_{n=1}^{2N} (-1)^n * n/(n+1)
    """
    total = 0
    for i in range(1, 2 * N + 1):
        term = (-1) ** i * i / (i + 1)
        total = total + term
    return total

def sum_S2(N):
    """计算第二种形式的级数和：两项求和相减
    S_N^(2) = -sum_{n=1}^N (2n-1)/(2n) + sum_{n=1}^N (2n)/(2n+1)
    """
    first_sum = 0
    second_sum = 0
    for j in range(1, N + 1):
        first_sum = first_sum + (2 * j - 1) / (2 * j)
        second_sum = second_sum + (2 * j) / (2 * j + 1)
    return -first_sum + second_sum

def sum_S3(N):
    """计算第三种形式的级数和：直接求和
    S_N^(3) = sum_{n=1}^N 1/(2n(2n+1))
    """
    result = 0
    for k in range(1, N + 1):
        denominator = 2 * k * (2 * k + 1)
        result = result + 1 / denominator
    return result

def calculate_relative_errors(N_values):
    """计算相对误差
    """
    error_1 = []
    error_2 = []
    for N in N_values:
        s1 = sum_S1(N)
        s2 = sum_S2(N)
        s3 = sum_S3(N)
        err1 = abs((s1 - s3) / s3)
        err2 = abs((s2 - s3) / s3)
        error_1.append(err1)
        error_2.append(err2)
    return error_1, error_2

def plot_errors(N_values, err1, err2):
    """绘制误差分析图
    """
    plt.figure(figsize=(10, 6))
    plt.loglog(N_values, err1, 'o-', label='S1误差', alpha=0.7)
    plt.loglog(N_values, err2, 's--', label='S2误差', alpha=0.7)

    plt.grid(True, which="both", ls="-", alpha=0.2)
    plt.xlabel('N')
    plt.ylabel('相对误差')
    plt.title('相对误差 vs N')
    plt.legend()

    plt.savefig('series_sum_errors.png', dpi=300, bbox_inches='tight')
    plt.show()

def print_results():
    """打印典型N值的计算结果
    """
    N_values = [10, 100, 1000, 10000]
    print("\n计算结果:")
    print("N\tS1\t\tS2\t\tS3\t\tErr1\t\tErr2")
    print("-" * 80)
    for N in N_values:
        s1 = sum_S1(N)
        s2 = sum_S2(N)
        s3 = sum_S3(N)
        err1 = abs((s1 - s3) / s3)
        err2 = abs((s2 - s3) / s3)
        print(f"{N}\t{s1:.8f}\t{s2:.8f}\t{s3:.8f}\t{err1:.2e}\t{err2:.2e}")

def main():
    """主函数
    """
    # 生成N值序列
    N_values = np.logspace(0, 4, 50, dtype=int)

    # 计算误差
    err1, err2 = calculate_relative_errors(N_values)

    # 打印结果
    print_results()

    # 绘制误差图
    plot_errors(N_values, err1, err2)

if __name__ == "__main__":
    main()
