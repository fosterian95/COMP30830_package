import os
import socket
import platform
import psutil
import timeit
import math
import itertools


def bench_pidigits(ndigits=1000, loops=100):

    def calc_ndigits(n):
    # Adapted from code on http://shootout.alioth.debian.org/
        def gen_x():
            return map(lambda k: (k, 4*k + 2, 0, 2*k + 1), itertools.count(1))

        def compose(a, b):
            aq, ar, as_, at = a
            bq, br, bs, bt = b
            return (aq * bq,
            aq * br + ar * bt,
            as_ * bq + at * bs,
            as_ * br + at * bt)

        def extract(z, j):
            q, r, s, t = z
            return (q*j + r) // (s*j + t)

        def pi_digits():
            z = (1, 0, 0, 1)
            x = gen_x()
            while 1:
                y = extract(z, 3)
                while y != extract(z, 4):
                    z = compose(z, next(x))
                    y = extract(z, 3)
                z = compose((10, -10*y, 0, 1), z)
                yield y

            return list(itertools.islice(pi_digits(), n))

    for _ in range(loops):
        calc_ndigits(ndigits)
        #print(âPi:â, ââ.join(map(str, calc_ndigits(ndigits))))
        return

def main():
    machine_name = socket.gethostname()
    operating_sytem = platform.system()
    operating_system_version = platform.version()
    cpu_number = os.cpu_count()
    memory_info = psutil.virtual_memory()[1]
    ip_addr = socket.gethostbyname(machine_name)

    system_info_message = f"The name of your machine is {machine_name}. " + f"Your current operating system is {operating_sytem} and the version is {operating_system_version}. " + f"Your machine has {cpu_number} CPUs. The total virtual memory of the machine is {memory_info}. " + f"Your current IP address is {ip_addr}."
    print (system_info_message)

    t_default = 6.388216104
    start_time = timeit.default_timer()
    bench_pidigits(ndigits=1000, loops=100)
    elapsed_time = timeit.default_timer() - start_time
    print("Relative elapsed time:", elapsed_time/t_default)

if __name__ == '__main__':
    main()

