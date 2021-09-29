# Jupiter Polar Vortex
## Todo
- [ ] track center positions of all vortices.
## Sep 29, 2021
### Redo the intruder experiment.
- a1: first test case (10 min).
1. [input file](fig_g_intruder.inp)
1. [vortex position file](intruder_85.txt)
```bash
mpiexec -n 64 ./polar_vortex.ex -i fig_g_intruder.inp > log.a1 &
```

