##  Benchmark examples

Benchmarks that replicate previous work using the capabilities of Underworld.

!!! hint "**Note**"

        <p/>Expand the boxes below to read more about each notebook and to view a preview.
        You can **run** these notebooks live on [http://www.mybinder.org]( {{nb_mybinder_location("notebooks/user_guide/00_Components.ipynb") }} ).

        {{ nb_mybinder_badge("notebooks/pulications/00_Pulications.ipynb") }}


### Moresi and Solomatov 1995

Stagnant lid convection model that demonstrates how to produce non-dimensional models with
a temperature dependent (Frank-Kamenetskii) viscosity and how to record Nusselt number and Vrms for a simulation in a way that transfers correctly to a parallel environment. Also demonstrates saving and restarting for long run-times.

Moresi, L. N., and V. S. Solomatov (1995), **Numerical investigation of 2d convection with extremely large viscosity variations**, Phys. Fluids, 7, 2154–2162.

??? note "**Notebook**"

    {{ embed_url_changeable("../../nb_html/publications/MoresiSolomatov-1995/MoresiAndSolomatov1995.html", fname="nb_frame_ms1995") }}


---

### Davies & Rawlinson, 2014

{{ figure("../../notebooks/images/DandRexample.png",
  fstyle="float:right; width:50%; border:1px; padding:10px; ",
  istyle="margin-left:10px; width:100%;",
  caption="Figure DR6 of Davies and Rawlinson (2014)") }}

This notebook reproduces the 2D instantaneous flow model with a composite Newtonian and non-Newtonian rheology shown in Figure DR6 of Davies and Rawlinson (2014). Rheological parameters are consistent with Karato and Wu (1993), with prefactors chosen to produce a minimum diffusion creep viscosity of $5 x 10^{19}$ Pa.s within the asthenosphere and dislocation creep dominating within the edge driven convection cell.

D. Rhodri Davies and Nicholas Rawlinson, **On the origin of recent intraplate volcanism in Australia**. Geology, December 2014, v. 42, p. 1031-1034, doi:10.1130/G36093.1

??? note "**Notebook**"
    {{ embed_url_changeable("../../nb_html/publications/DaviesRawlinson-2014/daviesRawlinson-2014-figDR6.html", fname="nb_frame_dr2014") }}

---

### Tosi et al, 2015 (Benchmark)

{{ figure("../../notebooks/images/TosiExample.png",
  fstyle="float:right; width:33%; border:1px; padding:10px; ",
  istyle="margin-left:10px; width:100%;",
  caption="") }}

This series of notebooks generates benchmark models from the Tosi et al. (2015) in Underworld2. The Underworld2 results are then directly compared to the results from Table 2 of Tosi et al. (2015) the paper for each case. The notebooks are broken into a general notebook for reproducing the models from scratch and 5 post-analysis notebooks which look at the results Underworld2 gives for each case after running to equilibrium.

Tosi, Nicola and Stein, Claudia and Noack, Lena and Hüttig, Christian and Maierová, Petra and Samuel, Henri and Davies, DR and Wilson, CR and Kramer, SC and Thieulot, Cedric and others. . **A community benchmark for viscoplastic thermal convection in a 2-D square box**, (2015)


??? note "**Notebooks**"
     <p/>

     - {{ replace_embedded_url(
       "../../nb_html/publications/TosiEtAl-2015/Tosi_Case1.html",
             "nb_frame_tetal2015",  
             "Tosi_Case1.ipynb") }}
     - {{ replace_embedded_url(
       "../../nb_html/publications/TosiEtAl-2015/Tosi_Case2.html",
            "nb_frame_tetal2015",  
            "Tosi_Case2.ipynb") }}
     - {{ replace_embedded_url(
       "../../nb_html/publications/TosiEtAl-2015/Tosi_Case3.html",
           "nb_frame_tetal2015",  
           "Tosi_Case3.ipynb") }}
     - {{ replace_embedded_url(
       "../../nb_html/publications/TosiEtAl-2015/Tosi_Case4.html",
          "nb_frame_tetal2015",  
          "Tosi_Case4.ipynb") }}
     - {{ replace_embedded_url(
       "../../nb_html/publications/TosiEtAl-2015/Tosi_Case5a.html",
          "nb_frame_tetal2015",  
          "Tosi_Case5a.ipynb") }}

     {{ embed_url_changeable("../../nb_html/publications/TosiEtAl-2015/Tosi_Case1.html", fname="nb_frame_tetal2015") }}


---


### OzBench et al, 2008


The Ozbench benchmark is used to compare 3D subduction models. The benchmark tests the ability to reproduce the deformation and retreat velocity of a single "slab" foundering in a large box of viscous fluid.
Viscous/plastic and viscoelastic/plastic models are catered for, with the appropriate equivalent parameter choices. The upper surface can be free-slip (no vertical movement) or a moving, stress-free interface. In the former case, some plasticity in the near-surface is needed to allow the slab to bend and detach from the surface. The Underworld example is for a slab with a viscous core and viscoplastic upper and lower layers and a free-slip upper boundary.
The 3D subduction model has a dense, high viscosity 3 layered plate overlying a lower viscosity mantle. The upper and lower plate layers have a visco-plastic rheology, yielding under large stresses. The middle, core layer has a viscous only rheology, maintaining strength during bending. The top 1000 km of the mantle is included, the upper & lower mantle is partitioned with a viscosity contrast of 100x at 600 km depth. The velocity boundary conditions on the domain are free-slip.

OzBench, M.; Regenauer-Lieb, K.; Stegman, D. R.; Morra, G.; Farrington, R.; Hale, A.; May, D. A.; Freeman, J.; Bourgouin, L.; Mühlhaus, H. & Moresi, L. **A model comparison study of large-scale mantle-lithosphere dynamics driven by subduction**. Physics of the Earth and Planetary Interiors, 2008, 171, 224-234


??? note "**Notebooks**"

    <p/>

    - {{ replace_embedded_url(
     "../../nb_html/publications/OzBenchEtAl-2008/1_OzBenchEtAl-2008.html",
           "nb_frame_ozbench2008",  
           "1_OzBenchEtAl-2008.ipynb") }}
    - {{ replace_embedded_url(
     "../../nb_html/publications/OzBenchEtAl-2008/2_OzBenchEtAl-2008-fig3.html",
          "nb_frame_ozbench2008",  
          "2_OzBenchEtAl-2008-fig3.ipynb") }}

    {{ embed_url_changeable("../../nb_html/publications/OzBenchEtAl-2008/1_OzBenchEtAl-2008.html", fname="nb_frame_ozbench2008") }}



---
