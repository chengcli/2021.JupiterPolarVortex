# Jupiter Polar Vortex
## Todo
- [x] track center positions of all vortices
- [x] print position into a table
- [ ] plot vortex positions

## Sep 29, 2021
### Redo the intruder experiment.
- a1: first test case (10 min).
1. [input file](fig_g_intruder.inp)
1. [vortex position file](intruder_85.txt)
```bash
mpiexec -n 64 ./polar_vortex.ex -i fig_g_intruder.inp > log.a1 &
```
### Put in realistic vortex positions [^1]
1. [sp vortices](sp161211.txt)
2. [sp input](sp161211.inp)

**south polar vortices:**
Based on PJ4 GRAV orbit (12/11/2016).
Vortex ID | Lat | Lon
--------- | --- | ---
S0 | 88.6 | 211.3
S1 | 83.7 | 157.1
S2 | 84.3 | 94.3
S3 | 85.0 | 13.4
S4 | 84.1 | 298.8
S5 | 83.2 | 229.7

**north polar vortices:**
Vortex ID | Lat | Lon
--------- | --- | ---
N0 | 89.6 | 230.4
N1 | 82.9 | 1.4
N2 | 83.8 | 50.7
N3 | 82.0 | 95.3
N4 | 83.2 | 137.6
N5 | 82.9 | 183.4
N6 | 83.2 | 227.6
N7 | 82.3 | 269.9
N8 | 83.5 | 314.8

- b1: first test case (~10 min)
```bash
mpiexec -n 64 ./polar_vortex.ex -i sp161211.inp > log.b1 &
```

## References
[^1]: Mura+, 2021
