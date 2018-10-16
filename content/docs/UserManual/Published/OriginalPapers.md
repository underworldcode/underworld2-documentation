##  Original work with Underworld

Novel research results
that arose from work with Underworld. The examples here demonstrate how to build upon
the original papers. Note that these are not exact replication of results from those papers.
We aim instead to show you examples that you can build on to advance the research.

!!! hint "**Note**"

        <p/>Expand the boxes below to read more about each notebook and to view a preview.
        You can **run** these notebooks live on [http://www.mybinder.org]( {{nb_mybinder_location("notebooks/user_guide/00_Components.ipynb") }} ).

        {{ nb_mybinder_badge("notebooks/pulications/00_Pulications.ipynb") }}


### Schellart et al, 2010

{{ figure("../../notebooks/publications/SchellartEtAl-2010/input/subduction-strainRate-7000km.png",
  fstyle="float:right; width:30%; border:1px; padding:10px; ",
  istyle="margin-left:10px; width:100%;",
  caption="Schellart et al figure with 7000km wide plate") }}


Subduction of oceanic lithosphere occurs through two modes: subducting plate motion and trench migration. Using a global subduction zone data set and three-dimensional numerical subduction models, we show that slab width (W) controls these modes and the partitioning of subduction between them. Subducting plate velocity scales with W2/3, whereas trench velocity scales with 1/W.

These findings explain the Cenozoic slowdown of the Farallon plate and the decrease in subduction partitioning by its decreasing slab width. The change from Sevier-Laramide orogenesis to Basin and Range extension in North America is also explained by slab width; shortening occurred during wide-slab subduction and overriding-plate–driven trench retreat, whereas extension occurred during intermediate to narrow-slab subduction and slab-driven trench retreat.


Schellart, W. P. and Stegman, D. R. and Farrington, R. J. and Freeman, J. and Moresi, L. **Cenozoic Tectonics of Western North America Controlled by Evolving Width of Farallon Slab**. Science, 16 July 2010, Vol. 329, Issue 5989, pp. 316-319


??? note "**Notebooks**"

     - {{ replace_embedded_url(
       "../../nb_html/publications/SchellartEtAl-2010/1_SchellartEtAl-Science-2010.html",
             "nb_frame_sch2010",  
             "1_SchellartEtAl-Science-2010.ipynb") }}
     - {{ replace_embedded_url(
       "../../nb_html/publications/SchellartEtAl-2010/2_SchellartEtAl-Science-2010-analysis.html",
            "nb_frame_sch2010",  
            "2_SchellartEtAl-Science-2010-analysis.ipynb") }}


     {{ embed_url_changeable("../../nb_html/publications/SchellartEtAl-2010/1_SchellartEtAl-Science-2010.html", fname="nb_frame_sch2010") }}

---

### Farrington et al, 2014

{{ figure("../../notebooks/publications/FarringtonEtAl-2014/input/devStressInv-eta2e4-mu8.5e2-dt650.png",
  fstyle="float:right; width:50%; border:1px; padding:10px; ",
  istyle="margin-left:10px; width:100%;",
  caption="Farrington et al - viscoelastic slab model") }}


This notebook models a two dimensional viscoelastic subducting plate, as outlined in Farrington et al, (2014). A dense, high viscosity 3 layered plate overlies a lower viscosity mantle. The upper and lower plate layers have a visco-plastic rheology, yielding under large stress. The middle, core layer has a viscoelastic rheology. The top 600 km of the upper mantle is included. The velocity boundary conditions on the domain are period side, free-slip top and no-slip bottom wall. This notebook reproduces the subducting plate shown in Figure 4(e), highlighting elastic stresses within the slab hinge.

Farrington, R. J., L.-N. Moresi, and F. A. Capitanio (2014), **The role of viscoelasticity in subducting plates**, Geochem. Geophys. Geosyst., 15, 4291–4304.


??? note "**Notebook**"

     <!-- If more are needed, add them here
     - {{ replace_embedded_url(
     "../../nb_html/publications/FarringtonEtAl-2014/FarringtonEtAl-2014.html",
          "nb_frame_rjf2014",  
          "FarringtonEtAl-2014.ipynb") }}
     -->
     {{ embed_url_changeable("../../nb_html/publications/FarringtonEtAl-2014/FarringtonEtAl-2014.html", fname="nb_frame_rjf2014") }}


### Beall et al., 2017

We consider lithospheric mantle and/or lower crust which is more dense than the asthenosphere. This density contrast drives viscous flow, though the way in which this dense material sinks is highly dependent in the middle crustal rheology, relative to the rheology of the denes material.

This notebook reproduces the primary model setup from *'Dripping or delamination? A range of mechanisms for removing the lower crust or lithosphere'* (2017) by Beall, Moresi and Stern in Geophysical Journal International.


*Dripping / Rayleigh-Taylor Instability (RTI)*


{{ figure("../../notebooks/publications/DrippingDelamination-BeallEtAl-2017/img/model_Lc_0.30_Etac_1.00e+00_D_0.00_timestep_40.png",
  fstyle="float:right; width:25%; border:1px; padding:10px; ",
  istyle="margin-left:10px; width:100%;",
  caption="") }}

Non-linear instability which grows by the thickening and thinning of the anomalous dense material. A change in thickness introduces deviatoric normal stresses at the lithospere-asthenosphere boundary, driving viscous flow and subsequently further thickening / thinning. The sinking velocity increases exponentially and later super-exponentially with time.

*RTI 'triggered' by a high amplitude perturbation*

{{ figure("../../notebooks/publications/DrippingDelamination-BeallEtAl-2017/img/model_Lc_0.30_Etac_1.00e-01_D_0.75_timestep_70.png",
  fstyle="float:right; width:25%; border:1px; padding:10px; ",
  istyle="margin-left:10px; width:100%;",
  caption="") }}

If a large perturbation to the lithopshere-asthenosphere interface is rapidly imposed, the subsequent dynamics differ to the classical RTI. The initial velocity is quicker and the rate at which the velocity grows is slightly higher. The morphology can also differ significantly from the classical RTI.

*Delamination*

{{ figure("../../notebooks/publications/DrippingDelamination-BeallEtAl-2017/img/model_Lc_1.00e-02_D_1.00_timestep_50.png",
  fstyle="float:right; width:25%; border:1px; padding:10px; ",
  istyle="margin-left:10px; width:100%;",
  caption="") }}


Delamination involves the peeling away of the dense material from the continental crust above. We will choose the definition that a delaminating body is able to accellerate with negligible shear-strain. In this case, deformation of the peeling material behaves like a bending sheet. These models can to characterise how the sinking velocity of a delaminating body evolves, including the confirmation that the velocity initially increases exponentially.


Beall, A. P., L. Moresi, and T. Stern (2017), **Dripping or delamination? A range of mechanisms for removing the lower crust or lithosphere**, Geophys. J. Int., 210(2), 671–692, doi:10.1093/gji/ggx202.


??? note "**Notebook**"

       <!-- If more are needed, add them here
       - {{ replace_embedded_url(
       "../../nb_html/publications/DrippingDelamination-BeallEtAl-2017/dripping_or_delamination.html",
             "nb_frame1",  
             "dripping_or_delamination.ipynb") }}
       -->
       {{ embed_url_changeable("../../nb_html/publications/DrippingDelamination-BeallEtAl-2017/dripping_or_delamination.html", fname="nb_frame_beall2017") }}
