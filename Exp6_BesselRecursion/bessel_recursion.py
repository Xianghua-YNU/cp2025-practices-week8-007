import numpy as np
import matplotlib.pyplot as plt
from scipy.special import spherical_jn

def bessel_up(x, lmax):
    """向上递推计算球贝塞尔函数
    
    Args:
        x: float, 自变量
        lmax: int, 最大阶数
        
    Returns:
        numpy.ndarray, 从0到lmax阶的球贝塞尔函数值
    """
    # 学生在此实现向上递推算法
    # 提示:
    # 1. 初始化结果数组
    # 2. 计算j_0和j_1的初始值
    # 3. 使用递推公式计算高阶项
    j0 = np.sin(x)/x                #定义初始函数
    j1 = np.sin(x)/(x**2) - np.cos(x)/x
    jl = [j0,j1]                    #建立列表
    for i in range(1,lmax):
        jl.append(((2*i + 1)/x)*jl[i] - jl[i-1])    #计算
    return np.array(jl)

def bessel_down(x, lmax, m_start=None):
    """向下递推计算球贝塞尔函数
    
    Args:
        x: float, 自变量
        lmax: int, 最大阶数
        m_start: int, 起始阶数，默认为lmax + 15
        
    Returns:
        numpy.ndarray, 从0到lmax阶的球贝塞尔函数值
    """
    # 学生在此实现向下递推算法
    # 提示:
    # 1. 设置足够高的起始阶数
    # 2. 初始化临时数组并设置初始值
    # 3. 使用递推公式向下计算
    # 4. 使用j_0(x)进行归一化
    if m_start is None:m_start = lmax + 15  #设置初始值
    jl = np.zeros(m_start+2)                #初始化列表
    jl[m_start] = 1
    jl[m_start+1] = 0
    for i in range(m_start,0,-1):
        jl[i-1] = ((2*i + 1)/x)*jl[i] - jl[i+1]
    j_0 = np.sin(x)/x
    normalization = j_0/jl[0]               #归一化
    j = jl[:lmax+1]*normalization
    return j

def plot_comparison(x, lmax):
    """绘制不同方法计算结果的比较图
    
    Args:
        x: float, 自变量
        lmax: int, 最大阶数
    """
    # 学生在此实现绘图功能
    # 提示:
    # 1. 计算三种方法的结果
    # 2. 绘制函数值的半对数图
    # 3. 绘制相对误差的半对数图
    # 4. 添加图例、标签和标题
    j_up = bessel_up(x, lmax)           #计算三种方法的结果
    j_down = bessel_down(x, lmax)
    l = np.arange(lmax + 1)
    j_scipy = spherical_jn(l, x)
    plt.figure(figsize=(10, 5))         #创建画布
    plt.subplot(121)                    #创建两个子图，现在操作第一个，函数值图
    plt.semilogy(l, np.abs(j_up),'o-',label='Up')
    plt.semilogy(l, np.abs(j_down),'s--',label='Down')
    plt.semilogy(l, np.abs(j_scipy),'k-',label='Scipy')
    plt.grid(True)                      #启用网格线
    plt.xlabel('l')                     #设立标题
    plt.ylabel('|j_l(x)|')
    plt.title(f'x = {x}')
    plt.legend()                        #设置图例
    plt.subplot(122)                    #操作第二个子图，误差图
    err_up = np.abs((j_up - j_scipy) / j_scipy)
    err_down = np.abs((j_down - j_scipy) / j_scipy)
    plt.semilogy(l, err_up,'o-',label='Up Error')
    plt.semilogy(l, err_down,'s--',label='Down Error')
    plt.grid(True)                      #启用网格线
    plt.xlabel('l')
    plt.ylabel('Relative Error')
    plt.title(f'x = {x}')
    plt.legend()                        #启用图例
    pass

def main():
    """主函数"""
    # 设置参数
    lmax = 25
    x_values = [0.1, 1.0, 10.0]
    
    # 对每个x值进行计算和绘图
    for x in x_values:
        plot_comparison(x, lmax)
        
        # 打印特定阶数的结果
        l_check = [3, 5, 8]
        print(f"\nx = {x}:")
        print("l\tUp\t\tDown\t\tScipy")
        print("-" * 50)
        for l in l_check:
            j_up = bessel_up(x, l)[l]
            j_down = bessel_down(x, l)[l]
            j_scipy = spherical_jn(l, x)
            print(f"{l}\t{j_up:.6e}\t{j_down:.6e}\t{j_scipy:.6e}")

if __name__ == "__main__":
    main()
