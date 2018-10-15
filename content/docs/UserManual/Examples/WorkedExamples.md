## Worked Examples

These examples are beginning-to-end walks through sample problems which can be developed into research tools. The examples generally start simple and become more complicated.

!!! hint "**Note**"

    <p/>Expand the boxes below to read more about each notebook and to view a preview.
    You can **run** these notebooks live on [http://www.mybinder.org]( {{nb_mybinder_location("notebooks/examples/0_00_Examples.ipynb") }} ).

    {{ nb_mybinder_badge("notebooks/examples/0_00_Examples.ipynb") }}



??? note "**Steady State Thermal Model** - 1_01_Steady_State_Heat.ipynb"

      <p/>Perhaps the simplest problem that Underworld can usefully solve
      {{embed_url("../../nb_html/examples/1_01_Steady_State_Heat.html")}}

??? note "**Constant Viscosity Convection**  - 1_02_Convection_Example.ipynb"

      <p/> Three related notebooks that address how we set up simple
      Rayleigh-Bénard convection experiments. The first is a generic
      convection model.
      {{embed_url("../../nb_html/examples/1_02_Convection_Example.html")}}

??? note "**Constant Viscosity Convection**  - 1_03_BlankenbachBenchmark.ipynb"

      <p/> Three related notebooks that address how we set up simple
      Rayleigh-Bénard convection experiments. The second is
      from the paper: _B. Blankenbach, F. Busse, U. Christensen, L. Cserepes, D. Gunkel, U. Hansen, H. Harder, G. Jarvis, M. Koch, G. Marquart, D. Moore, P. Olson, H. Schmeling and T. Schnaubelt. A benchmark comparison for mantle convection codes. Geophysical Journal International, 98, 1, 23–38, 1989_
      {{embed_url("../../nb_html/examples/1_03_BlankenbachBenchmark.html")}}

??? note "**Constant Viscosity Convection**  - 1_04_BlankenbachBenchmark_Case2a.ipynb"

      <p/> Three related notebooks that address how we set up simple
      Rayleigh-Bénard convection experiments. The third is
      another case from the paper: _B. Blankenbach, F. Busse, U. Christensen, L. Cserepes, D. Gunkel, U. Hansen, H. Harder, G. Jarvis, M. Koch, G. Marquart, D. Moore, P. Olson, H. Schmeling and T. Schnaubelt. A benchmark comparison for mantle convection codes. Geophysical Journal International, 98, 1, 23–38, 1989_
      {{embed_url("../../nb_html/examples/1_04_BlankenbachBenchmark_Case2a.html")}}


??? note "**Sinking blob** - 1_05_StokesSinker.ipynb"

      <p/> Introducing the tracking of compositional variations by using a particle swarms with different material properties. This system consists of a dense, high viscosity sphere falling through a background lower density and viscosity fluid.
      {{embed_url("../../nb_html/examples/1_05_StokesSinker.html")}}

??? note "**Rayleigh-Taylor instability** - 1_06_Rayleigh_Taylor.ipynb"   

      <p/> The classical instability problem - in this case the benchmark
      Rayleigh-Taylor instability outlined in van Keken et al. (1997). _(van Keken, P.E.,
        S.D. King, H. Schmeling, U.R. Christensen, D.Neumeister and M.-P. Doin. A comparison of methods for the modeling of thermochemical convection. Journal of Geophysical Research, 102, 22,477-22,495, 1997.)_
        {{embed_url("../../nb_html/examples/1_06_Rayleigh_Taylor.html")}}


??? note "**Subduction Zone Model** - 1_07_SlabSubduction.ipynb"  

      <p/>This two dimensional subduction model has a dense, high viscosity 3 layered plate overlying a lower viscosity mantle. The upper and lower plate layers have a visco-plastic rheology, yielding under large stresses. The middle, core layer has a viscous only rheology, maintaining strength during bending. The top 1000 km of the mantle is included, the upper & lower mantle is partitioned with a viscosity contrast of 100x at 600 km depth. The velocity boundary conditions on the domain are period side, free-slip top and no-slip bottom wall.
      {{embed_url("../../nb_html/examples/1_07_SlabSubduction.html")}}

??? note "**Groundwater Flow** - 1_13_Groundwater_Flow.ipynb"

      <p/> Three related notebooks that address Darcy flow models for the crust. The first
      demonstrates how to set up the problem. The second introduces mesh-deformation to
      provide topographic forcing of the flow, and the last of these adds thermal effects.
      {{embed_url("../../nb_html/examples/1_13_Groundwater_Flow.html")}}


??? note "**Groundwater Flow** - 1_16_Groundwater_Topography.ipynb"

      <p/> Three related notebooks that address Darcy flow models for the crust. The first
      demonstrates how to set up the problem. The second introduces mesh-deformation to
      provide topographic forcing of the flow, and the last of these adds thermal effects.
      {{embed_url("../../nb_html/examples/1_16_Groundwater_Topography.html")}}

??? note "**Groundwater Flow** - 1_17_Groundwater_Flow_Temperature_Advection.ipynb"

      <p/> Three related notebooks that address Darcy flow models for the crust. The first
      demonstrates how to set up the problem. The second introduces mesh-deformation to
      provide topographic forcing of the flow, and the last of these adds thermal effects.
      {{embed_url("../../nb_html/examples/1_17_Groundwater_Flow_Temperature_Advection.html")}}


??? note "**Scaling / Non-dimensionalisation** - 1_14_ScalingExample.ipynb"    

      <p/>The Underworld scaling module leverages Pint, a python package used to define and manipulate physical units. Pint uses a system of unit registries to define a large set of units and most of their prefixes. Use of suitable scaling is recommended to improve numerical quality and to make models more versatile. A formal strategy for scaling is essential to prevent mistakes and help others understand the code.
      {{embed_url("../../nb_html/examples/1_14_ScalingExample.html")}}


??? note "**Thermo-chemical Convectionn** - 1_18_ThermochemicalConvection.ipynb"

      <p/>This notebook models the entrainment of a thin dense layer by
      thermochemical convection as outlined in van Keken *et al.* (1997).

      \begin{align*}
          \nabla \cdot \left( \eta \nabla \dot\varepsilon \right) - \nabla p &= (Ra T - Rb \Gamma )\mathbf{\hat z} \\\\
          \nabla \cdot \mathbf{u} &= 0
      \end{align*}

      where $Ra$ and $Rb$ are the thermal and compositional Rayleigh numbers (see _van Keken, P.E., S.D. King, H. Schmeling, U.R. Christensen, D.Neumeister and M.-P. Doin. A comparison of methods for the modeling of thermochemical convection. Journal of Geophysical Research, 102, 22,477-22,495, 1997._)  
      {{embed_url("../../nb_html/examples/1_18_ThermochemicalConvection.html")}}



!!! hint "**More Advanced Examples**"

          <p/>The following examples introduce more complex workflows, complicated rheology. It is certainly worthwhile addressing these ones after the section above. You can **run** these notebooks live on [http://www.mybinder.org]( {{nb_mybinder_location("notebooks/examples/0_00_Examples.ipynb") }} ).

          {{ nb_mybinder_badge("notebooks/examples/0_00_Examples.ipynb") }}


??? note "**Shear band formation**  - 2_08_ShearBandsSimpleShear.ipynb"

      <p/> Two related notebooks that show the formation of shear bands in a material with pressure-sensitive
      yield strength (a frictional material like sand, for example). The first notebook sets up a simple shear experiment in a periodic domain. We visualise and analyse the results in a way that works if the notebook (script) is run in parallel.
      {{embed_url("../../nb_html/examples/2_08_ShearBandsSimpleShear.html")}}


??? note "**Shear band formation** - 2_09_ShearBandsPureShear.ipynb"
      <p/> Two related notebooks that show the formation of shear bands in a material with pressure-sensitive
      yield strength (a frictional material like sand, for example). The second example is a pure-shear experiment that might serve as the starting point for extension models. We visualise and analyse the results in a way that works if the notebook (script) is run in parallel.
      {{embed_url("../../nb_html/examples/2_09_ShearBandsPureShear.html")}}


??? note "**Introducting Viscoelasticity**" - 2_11_ViscoelasticityInSimpleShear.ipynb"   

    <p/> This notebook reproduces figure 1a of Farrington et al (2014). All material is viscoelastic with equal parameters, differing material indices are prescribed for visualisation purposes. The vertical velocity bc is periodic, the bottom velocity bc is no-slip with a horizontal shear velocity bc applied to the top wall until $t = 1$.  For $t > 1$ the top wall velocity bc is no-slip.

      - sets $\eta_\textrm{eff}$ for viscoelastic materials
      - ensures a maximum timestep of $\Delta t_e / 3$
      - modifies stess to include history terms
      - updates stress history term on each particle
      - includes viscoelastic force term

    Farrington, R. J., L.-N. Moresi, and F. A. Capitanio (2014), The role of viscoelasticity in subducting plates, Geochem. Geophys. Geosyst., 15, 4291–4304, doi:10.1002/2014GC005507.

    {{embed_url("../../nb_html/examples/2_11_ViscoelasticityInSimpleShear.html")}}


??? note "**Rayleigh-Taylor - detailed analysis**" - 2_15_Rayleigh_Taylor_GrowthRate.ipynb"   

    <p/> Here we quantify the initial growth-rate of a Rayleigh-Taylor Instability,
    introduced in the previous Rayleigh-Taylor example.

    The model set up is shown below, where we are interested in the development of the perturbation $w$. The upper layer represents cold and subsequently dense (large $\rho$) and strong (large $\mu$) lithosphere (relative to the asthenosphere). We will quantify how quickly an instability with a particular wavelength will develop and compare this to an analytic solution.
    {{embed_url("../../nb_html/examples/2_15_Rayleigh_Taylor_GrowthRate.html")}}


??? note "**Numerical Convergence & analytic solutions**" - 2_19_Analytic_Solutions_2D.ipynb"  

    <p/> Underworld provides a set of analytic solutions to Stokes flow problems. In this example, analytic solution objects are used to configure an analogous numerical system. The numerical solution may then be compared to the exact solution (again provided by the analytic solution object). The first part of this file considers a single analytic model and the corresponding numerical solution. We then run a series simulations across different resolutions to extract error convergence information. This second part is repeated for a set of analytic models.
    {{embed_url("../../nb_html/examples/2_19_Analytic_Solutions_2D.html")}}
