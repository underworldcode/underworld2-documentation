# Underworld 2 - Live Manual & Tutorial


![Montage.png](./images/Montage.png)

[_Underworld 2_](http://www.underworldcode.org) is a python-friendly version of the Underworld code which provides a programmable and flexible front end to all the functionality of the code running in a parallel HPC environment. This gives signficant advantages to the user, with access to the power of python libraries for setup of complex problems, analysis at runtime, problem steering, and multi physics coupling. While Underworld2 embraces Jupyter Notebooks as the preferred modelling environment, only standard python is required.

The Underworld2 development team is based in Melbourne, Australia at the University of Melbourne and at Monash University led by Louis Moresi. We would like to acknowledge AuScope Simulation, Analysis and Modelling for providing long term funding which has made the project possible. Additional funding for specific improvements and additional functionality has come from the Australian Research Council (http://www.arc.gov.au). The python toolkit was funded by the NeCTAR eresearch_tools program. Underworld was originally developed in collaboration with the Victorian Partnership for Advanced Computing.


**The jupyter notebooks provided as examples are given below**

## User guide

The Underworld User Guide is a great introduction to the basic building blocks of the Underworld software suite. We cover the individual concepts in the code and provide simple notebooks to illustrate how to use them.

  - [01 Getting started        ](user_guide/01_GettingStarted.ipynb)
  - [02 Meshes                 ](user_guide/02_TheMesh.ipynb)
  - [03 Mesh based variables   ](user_guide/03_MeshVariable.ipynb)
  - [04 Swarms (of particles   ](user_guide/04_Swarms.ipynb)  
  - [05 Functions              ](user_guide/05_Functions.ipynb)  
  - [06 Equation systems       ](user_guide/06_Systems.ipynb)  
  - [07 Utilities              ](user_guide/07_Utilities.ipynb)  
  - [08 Visualisation          ](user_guide/08_Visualisation.ipynb)
  - [09 Stokes solver (Instructions)](user_guide/09_StokesSolver.ipynb)


## Examples

Examples are beginning-to-end walks through sample problems which can be developed into research tools. The examples
generally start simple and become more complicated.

  - [01  Steady State Heat Diffusion           ](examples/1_01_Steady_State_Heat.ipynb)
  - [02  Convection Example                    ](examples/1_02_Convection_Example.ipynb)
  - [03  Blankenbach et al Benchmark           ](examples/1_03_BlankenbachBenchmark.ipynb)
  - [04  Blankenbach et al Benchmark Case2a    ](examples/1_04_BlankenbachBenchmark_Case2a.ipynb)
  - [05  Stokes Sinker                         ](examples/1_05_StokesSinker.ipynb)
  - [06  Rayleigh_Taylor Instability           ](examples/1_06_Rayleigh_Taylor.ipynb)
  - [07  Slab Subduction                       ](examples/1_07_SlabSubduction.ipynb)
  - [13  Groundwater Flow                      ](examples/1_13_Groundwater_Flow.ipynb)
  - [14  Scaling Example                       ](examples/1_14_ScalingExample.ipynb)
  - [16  Groundwater flow and topography       ](examples/1_16_Groundwater_Topography.ipynb)
  - [17  Groundwater flow: Thermal Advection   ](examples/1_17_Groundwater_Flow_Temperature_Advection.ipynb)
  - [18  Thermochemical Convection             ](examples/1_18_ThermochemicalConvection.ipynb)

#### Advanced examples

  - [2 08_ShearBandsSimpleShear.ipynb                 ](examples/2_08_ShearBandsSimpleShear.ipynb)
  - [2 09_ShearBandsPureShear.ipynb                   ](examples/2_09_ShearBandsPureShear.ipynb)
  - [2 11_ViscoelasticityInSimpleShear.ipynb          ](examples/2_11_ViscoelasticityInSimpleShear.ipynb)
  - [2 15_Rayleigh_Taylor_GrowthRate.ipynb            ](examples/2_15_Rayleigh_Taylor_GrowthRate.ipynb)
  - [2 19_Analytic_Solutions_2D.ipynb                 ](examples/2_19_Analytic_Solutions_2D.ipynb)


## Tutorials

These tutorials are linked sets of notebooks that work through a problem from scratch and teach both the code and the underlying modelling problem. It can take a few hours to work through the whole thing and this may be better attempted in a local installation of Underworld (see [installation](#Underworld-Installation) below)

  - [Convection Tutorial     ](tutorials/ConvectionTutorial/Notebooks/000-Overview.ipynb)
  - [Viscoelasticity Tutorial](tutorials/ViscoelasticTutorial/010-Overview.ipynb)
  - [Basin Framework         ](tutorials/BasinFrameworkTutorial)


## Reproducing published results

Some of these are benchmarks that verify the capabilities of Underworld, others are novel research results
that arose from work with Underworld.

### Moresi and Solomatov 1995 (Benchmark)

Stagnant lid convection model that demonstrates how to produce non-dimensional models with
a temperature dependent (Frank-Kamenetskii) viscosity and how to record Nusselt number and Vrms for a simulation in a way that transfers correctly to a parallel environment. Also demonstrates saving and restarting for long run-times.

Moresi, L. N., and V. S. Solomatov (1995), **Numerical investigation of 2d convection with extremely large viscosity variations**, Phys. Fluids, 7, 2154–2162.

   - [Notebook 1 - convection model](./publications/MoresiSolomatov-1995/MoresiAndSolomatov1995.ipynb)

---

### Davies & Rawlinson, 2014  (Benchmark)


<figure>
  <img src="images/DandRexample.png" width="35%" style="float:right;" >
</figure>

This notebook reproduces the 2D instantaneous flow model with a composite Newtonian and non-Newtonian rheology shown in Figure DR6 of Davies and Rawlinson (2014). Rheological parameters are consistent with Karato and Wu (1993), with prefactors chosen to produce a minimum diffusion creep viscosity of $5 x 10^{19}$ Pa.s within the asthenosphere and dislocation creep dominating within the edge driven convection cell.

D. Rhodri Davies and Nicholas Rawlinson, **On the origin of recent intraplate volcanism in Australia**. Geology, December 2014, v. 42, p. 1031-1034, doi:10.1130/G36093.1

   - [Notebook: Figure 6](publications/DaviesRawlinson-2014/daviesRawlinson-2014-figDR6.ipynb)

---

### Tosi et al, 2015 (Benchmark)


Tosi, Nicola and Stein, Claudia and Noack, Lena and Hüttig, Christian and Maierová, Petra and Samuel, Henri and Davies, DR and Wilson, CR and Kramer, SC and Thieulot, Cedric and others. . **A community benchmark for viscoplastic thermal convection in a 2-D square box**, (2015)

<figure>
  <img src="images/TosiExample.png" width="12%" style="float:right;" >
</figure>



   - [Notebook: Case1](publications/TosiEtAl-2015/Tosi_Case1.ipynb)
   - [Notebook: Case2](publications/TosiEtAl-2015/Tosi_Case2.ipynb)
   - [Notebook: Case3](publications/TosiEtAl-2015/Tosi_Case3.ipynb)
   - [Notebook: Case4](publications/TosiEtAl-2015/Tosi_Case4.ipynb)
   - [Notebook: Case5a](publications/TosiEtAl-2015/Tosi_Case5a.ipynb)

---


### OzBench et al, 2008


The Ozbench benchmark is used to compare 3D subduction models. The benchmark tests the ability to reproduce the deformation and retreat velocity of a single "slab" foundering in a large box of viscous fluid.
Viscous/plastic and viscoelastic/plastic models are catered for, with the appropriate equivalent parameter choices. The upper surface can be free-slip (no vertical movement) or a moving, stress-free interface. In the former case, some plasticity in the near-surface is needed to allow the slab to bend and detach from the surface. The Underworld example is for a slab with a viscous core and viscoplastic upper and lower layers and a free-slip upper boundary.
The 3D subduction model has a dense, high viscosity 3 layered plate overlying a lower viscosity mantle. The upper and lower plate layers have a visco-plastic rheology, yielding under large stresses. The middle, core layer has a viscous only rheology, maintaining strength during bending. The top 1000 km of the mantle is included, the upper & lower mantle is partitioned with a viscosity contrast of 100x at 600 km depth. The velocity boundary conditions on the domain are free-slip.

OzBench, M.; Regenauer-Lieb, K.; Stegman, D. R.; Morra, G.; Farrington, R.; Hale, A.; May, D. A.; Freeman, J.; Bourgouin, L.; Mühlhaus, H. & Moresi, L. **A model comparison study of large-scale mantle-lithosphere dynamics driven by subduction**. Physics of the Earth and Planetary Interiors, 2008, 171, 224-234

   - [Notebook 1 - Setup](publications/OzBenchEtAl-2008/1_OzBenchEtAl-2008.ipynb)
   - [Notebook 2 - Figure 3](publications/OzBenchEtAl-2008/2_OzBenchEtAl-2008-fig3.ipynb)


---

### Schellart et al, 2010

<figure>
  <img src="publications/SchellartEtAl-2010/input/subduction-strainRate-7000km.png" width="30%" style="float:right;" >
</figure>

Subduction of oceanic lithosphere occurs through two modes: subducting plate motion and trench migration. Using a global subduction zone data set and three-dimensional numerical subduction models, we show that slab width (W) controls these modes and the partitioning of subduction between them. Subducting plate velocity scales with W2/3, whereas trench velocity scales with 1/W.

These findings explain the Cenozoic slowdown of the Farallon plate and the decrease in subduction partitioning by its decreasing slab width. The change from Sevier-Laramide orogenesis to Basin and Range extension in North America is also explained by slab width; shortening occurred during wide-slab subduction and overriding-plate–driven trench retreat, whereas extension occurred during intermediate to narrow-slab subduction and slab-driven trench retreat.


Schellart, W. P. and Stegman, D. R. and Farrington, R. J. and Freeman, J. and Moresi, L. **Cenozoic Tectonics of Western North America Controlled by Evolving Width of Farallon Slab**. Science, 16 July 2010, Vol. 329, Issue 5989, pp. 316-319

   - [Notebook 1 - Computations](publications/SchellartEtAl-2010/1_SchellartEtAl-Science-2010.ipynb)
   - [Notebook 2 - Analysis](publications/SchellartEtAl-2010/2_SchellartEtAl-Science-2010-analysis.ipynb)


---

<!-- FROM Rohan ?
   - Moresi, L., Moresi, L. N., and V. S. Solomatov (1998), **Mantle convection with a brittle lithosphere: thoughts on the global tectonic styles of the Earth and Venus**, Geophysicical Journal International, 133(3), 669–682, doi:10.1046/j.1365-246X.1998.00521.x.
-->

### Farrington et al, 2014

<figure>
  <img src="publications/FarringtonEtAl-2014/input/devStressInv-eta2e4-mu8.5e2-dt650.png" width="40%" style="float:right;" >
</figure>

This notebook models a two dimensional viscoelastic subducting plate, as outlined in Farrington et al, (2014). A dense, high viscosity 3 layered plate overlies a lower viscosity mantle. The upper and lower plate layers have a visco-plastic rheology, yielding under large stress. The middle, core layer has a viscoelastic rheology. The top 600 km of the upper mantle is included. The velocity boundary conditions on the domain are period side, free-slip top and no-slip bottom wall. This notebook reproduces the subducting plate shown in Figure 4(e), highlighting elastic stresses within the slab hinge.

Farrington, R. J., L.-N. Moresi, and F. A. Capitanio (2014), **The role of viscoelasticity in subducting plates**, Geochem. Geophys. Geosyst., 15, 4291–4304.

   - [Notebook 1](publications/FarringtonEtAl-2014/FarringtonEtAl-2014.ipynb)


### Beall et al., 2017

We consider lithospheric mantle and/or lower crust which is more dense than the asthenosphere. This density contrast drives viscous flow, though the way in which this dense material sinks is highly dependent in the middle crustal rheology, relative to the rheology of the denes material.

This notebook reproduces the primary model setup from *'Dripping or delamination? A range of mechanisms for removing the lower crust or lithosphere'* (2017) by Beall, Moresi and Stern in Geophysical Journal International.


*Dripping / Rayleigh-Taylor Instability (RTI)*

<figure>
  <img src="publications/DrippingDelamination-BeallEtAl-2017/img/model_Lc_0.30_Etac_1.00e+00_D_0.00_timestep_40.png" style="width: 25%; float:right;" />
</figure>

Non-linear instability which grows by the thickening and thinning of the anomalous dense material. A change in thickness introduces deviatoric normal stresses at the lithospere-asthenosphere boundary, driving viscous flow and subsequently further thickening / thinning. The sinking velocity increases exponentially and later super-exponentially with time.


*RTI 'triggered' by a high amplitude perturbation*

<figure>
  <img src="publications/DrippingDelamination-BeallEtAl-2017/img/model_Lc_0.30_Etac_1.00e-01_D_0.75_timestep_70.png" style="width: 25%; float:right;" />
</figure>

If a large perturbation to the lithopshere-asthenosphere interface is rapidly imposed, the subsequent dynamics differ to the classical RTI. The initial velocity is quicker and the rate at which the velocity grows is slightly higher. The morphology can also differ significantly from the classical RTI.

*Delamination*

<figure>
  <img src="publications/DrippingDelamination-BeallEtAl-2017/img/model_Lc_1.00e-02_D_1.00_timestep_50.png" style="width: 25%; float:right;" />
</figure>

Delamination involves the peeling away of the dense material from the continental crust above. We will choose the definition that a delaminating body is able to accellerate with negligible shear-strain. In this case, deformation of the peeling material behaves like a bending sheet. These models can to characterise how the sinking velocity of a delaminating body evolves, including the confirmation that the velocity initially increases exponentially.


Beall, A. P., L. Moresi, and T. Stern (2017), **Dripping or delamination? A range of mechanisms for removing the lower crust or lithosphere**, Geophys. J. Int., 210(2), 671–692, doi:10.1093/gji/ggx202.

   - [Notebook 1](publications/DrippingDelamination-BeallEtAl-2017/dripping_or_delamination.ipynb)


## Underworld Installation

If you decide to run this tutorial on your own machine and want to build new examples, you can most easily install underworld from the docker container.


Most new users may wish to use the [Kitematic GUI](https://github.com/docker/kitematic/releases) to download and run Underworld. Simply search for 'underworldcode/underworld2' within Kitematic, and then click 'CREATE' to launch a container. You will eventually wish to modify your container settings (again through Kitematic) to enable local folder volume mapping, which will allow you to access your local drives within your container.

For Linux users, and those who prefer the command line, the following minimal command should be sufficient to access the Underworld2 Jupyter Notebook examples:

```bash
   docker run --rm -p 8888:8888 underworldcode/underworld2
```
Navigate to `localhost:8888` to see the notebooks.

### Build health


| Version | Status |
| :----   | :----  |
| Lastest stable release (master branch) | [![Build Status](http://130.56.252.251:32779/buildStatus/icon?job=master)](http://130.56.252.251:32779/job/master/) |
| Development branch | [![Build Status](http://130.56.252.251:32779/buildStatus/icon?job=uw-dev)](http://130.56.252.251:32779/job/uw-dev/) |
