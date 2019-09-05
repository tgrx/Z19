d_c_t = {
    "zyndel": "qwerty",
    "master": 123,
    "alexander": "*12qw",
    "artem": 55567,
    "egor": [1, 5, 7],
    "lol": 17,
    "bugaGA": (1, 3, 6),
}
s_t_r0 = "xdcfvgbhnxdcfvgkbh23645677osedrfutgiyhpouiylukj6seydrufvkbugaGa"


# %timeit 'bugaGA' in d_c_t
# 50.1 ns ± 0.809 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
#
# %timeit 'bugaGA' in s_t_r0
# 85.6 ns ± 0.293 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)


i_n_t = 768543268543126453127645312645312645312 * 64531645316745316784531645312678453
f_l_t = (
    768543268543126453127645312645312645312.0 * 64531645316745316784531645312678453.0
)
c_m_p_l = (645324568753214568532 + 76453547867543j) * (
    21524562135468535468532563256 - 215573463455687435442542554j
)
s_t_r1 = "xdcfuvgihbzsxcfvgkbhxhcfjvg" * 78457


# %timeit i_n_t
# 26.5 ns ± 0.302 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
#
# %timeit f_l_t
# 30.7 ns ± 0.173 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
#
# %timeit c_m_p_l
# 34.7 ns ± 0.336 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
#
# %timeit  s_t_r1
# 26.2 ns ± 0.294 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)


s_t_r2 = "HelloMyDearFriend"
l_s_t = list(s_t_r2)
t_p_l = tuple(s_t_r2)


# %timeit 'i' in s_t_r2
# 60.2 ns ± 0.422 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
#
# %timeit 'i' in l_s_t
# 306 ns ± 19.9 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
#
# %timeit 'i' in t_p_l
# 283 ns ± 2.55 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
