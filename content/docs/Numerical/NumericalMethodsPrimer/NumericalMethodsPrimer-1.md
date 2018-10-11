
## Computational Geodynamics: Introduction to Numerical Methods

\\[
\require{color}
\newcommand{\dGamma}{\mathbf{d}\boldsymbol{\Gamma}}
\newcommand{\erfc}{\mbox{\rm erfc}}
\newcommand{\curly}{\sf }
\newcommand{\Red}[1]{\textcolor[rgb]{0.7,0.0,0.0}{\#1}}
\newcommand{\Green}[1]{\textcolor[rgb]{0.0,0.7,0.0}{ \#1}}
\newcommand{\Blue}[1]{\textcolor[rgb]{0.0,0.0,0.7}{ \#1}}
\newcommand{\Emerald}[1]{\textcolor[rgb]{0.0,0.7,0.3}{ \#1}}
\newcommand{\curly}
\\]



## Introductory Remarks

We have considered the application of mathematical reasoning to construct models of the behaviour of physical systems. Unfortunately, most of these models do not have analytic solutions or the solutions are so complicated that they don't help us understand the problem. The alternative is to solve such problems numerically (approximately). Such solutions are also possible for far more elaborate systems than we would even consider trying to obtain exact solutions for.

On the other hand, numerical modeling only provides solutions to mathematical equations and only approximate solutions at that. Unless the modeler has an understanding of the methods and the models themselves, then the output of some computer code may be terribly misleading.

It is always necessary to design a numerical experiment as carefully as one would a physical experiment --- although it won't blow up and kill you. It is possible to change the laws of physics in the numerical model often inadvertantly, so a careful analysis of the problem first is not a bad idea.

This part of the course contains some really hard material. This is deliberate because the workings of most computer codes are actually based on some astonishingly intricate mathematics. This is really intended to provide a decent reference for people coming back to use finite elements or other numerical methods later.

## A Variety of Numerical Methods

We will discuss a number of different numerical solution techniques which are suitable for solid Earth dynamics problems. Obviously only a brief discussion of any one method is possible, and more methods are inevitably available.

Some methods work well for particular problem and others roll over and die with hardly any sign of impending doom. We need to know what the tools in our toolbox are for and what will cause them to break before we try to solve serious problems with them. After all, in uncharted territory, a numerical  instability might look enticingly like an exiting new result.

Obviously there is not room to do justice to any particular method and I will concentrate on how the finite element method works (though for some things other methods have many advantages).

### Finite Differences

If we have encountered calculus at all, then we are already familiar with finite differences. Where we would, in determining a derivative, consider the limit of a quantity over a small interval as that interval shrinks to an infinitessimal size, in finite differences, we compute the value of such quantities for small, finite intervals. Typically we use regular _meshes_ of points on which to compute the differences (but we don't have to !).

Finite Difference methods are simple and can be very fast. They can be intuitively easy to understand and program and are also universally applied. They may encounter difficulties when extreme variations in properties occur from one grid point to another, particularly if there are discontinuities.

### Finite Elements

Finite elements work from a variational principle (more, much more, later) which is an integral version of the governing equations. They work with a spatial discretization into a mesh spanned by elements with unknowns allocated to their vertices.

The application of finite elements to complex problems and those with very complex domains is a programmers joy since the entire methodology match  object - oriented programming techniques. The flip-side of this is that the construction of the numerical equations which need to be solved may take considerably longer than the actual solution process.

The retention of the integral form can be beneficial for problems with difficult boundary conditions or discontinuities which can be integrated. Variational methods are, however, difficult to constrain particularly when iterative, implicit solution methods are used.

### Finite Volumes

In finite volumes one combines some of the best features of finite elements and finite differences. The method is grid based and works with both the original mesh and its dual. The formulation starts with a weak form of the equations based on volume fluxes into the local volume surrounding a node (based on the dual mesh). These integrals are then converted via Gauss' theorem, into surface integrals on the edges/faces of the dual mesh. Depending on the subsequent discretization, the resulting algorithm can be akin to finite differences or to finite elements (whether surface integrals remain in the formulation or are replaced by some differencing form) Advantages include the fact that the surface integral formulation can be tailored to satisfy local constraints without additional messing about thus making for very rapid solution times. The formulation can also deal with arbitrary mesh configurations. Disadvantages include a difficulty in applying some boundary conditions since the dual surface is not defined outside the mesh (formally).

### Natural Elements

An extension of finite elements using the theory of Natural Neighbour interpolation schemes to provide shape functions for all grid point arrangements. A best (Delaunay) triangulation is defined for such a set of points and interpolation functions exist which give an optimal representation of the interpolant. These functions can provide a basis for a finite element scheme. Advantages include the fact that elements can be highly distorted but this does not affect the convergence of the method in the same catastrophic way as for normal schemes. Disadvantages include the fact that shape functions overlap other elements and therefore precise integration is difficult. Also this is a relatively novel method and there are some odds and ends to be ironed out.

### Spectral (time/space)

We saw in the theoretical treatment of instabilities in a layer how beneficial it can be to deal with harmonic functions in one or more dimensions. This turns the problem from a partial differential equation into a set of ordinary differential equations for the different wavenumbers. The method works well for systems with homogeneous material properties otherwise spatial variations in these properties are couple the different wavenumbers together and add layer upon layer of complexity to the problem. Due to the existence of the fast fourier transform, these methods, when they can be applied, are potentially very quick. They are limited to relatively regular geometries, however.

### Discrete Elements

Meshless methods which deal with either actual discrete systems such as large systems of granular materials or systems in which notional particles represent elements of the continuum.  The method works by treating simple interactions of very many particles dynamically. For each particle an explicit solution of $F=ma$ for translations and $L=I\ddot{\theta}$ for the rotations is found in reponse to the interaction forces with every other particle. In discrete elements such interactions are usually local (e.g. only when particles are in contact) and this makes the system manageable in size.  Very good for treatment of fracture and dynamic responses of granular systems but can be hampered by the time taken for the fully explicit nature of the algorithm, i.e. elastic waves must be resolved in order to  model deformation. Also, these methods are based on particle interaction functions and so properties of the continuum such as viscosity are not direct inputs but have to be computed as an average response of the system (just like the real thing). _Compare this to molecular dynamics simulations._

### Smooth Particle Hydrodynamics

Another meshless method in which "particles" are the centres of smooth functions such as gaussians. These can be used to interpolate any field across the solution domain. They are also differentiable and can therefore represent differential equations relatively efficiently. Very useful for high velocity flows and astrophysics type problems. Historically there have been problems representing boundary conditions and viscosity so not ideal for the highly viscous and/or elastic type problems of the solid earth.

### Particle in Cell methods

In these methods both particles and a mesh exist. The mesh supplies the velocities which move particles around, but the particles carry information with them in a Lagrangian sense. Derivatives are computed on the mesh using the values of nodal variables but material property variations are measured by the particles. Advantages include the fact that the method is geometrically simple for relatively complex deformations and uses a horses-for-courses approach with the mesh doing what it is best at - derivatives, fast solutions and the particles doing their part on the Lagrangian components of the problem. Major disadvantages include the fact that the particle properties and the mesh properties must be synchronized and this may involve some averaging to the mesh. Worse, there need to be more particles than grid points for the algorithm to work, but this means there are more particle degrees of freedom than can be constrained by the mesh --- this means that multiple particle configurations can produce the same solution on the mesh some of which may be unstable and incapable of being damped during the solution.

### Lagrangian/Eulerian meshes

As we hinted earlier, Lagrangian formulations eliminate convective terms from the equations but at the expense of geometrical complexity. Finite elements are not particularly troubled by complex meshes provided the elements do not become too distorted. Thus, for moderate deformations, advection of the grid points provides a simple way to eliminate the much more complicated advection terms from the differential equations. For fluids, however, the deformation ultimately ruins the ability of the mesh to converge on the correct solution and the results have to be interpolated to a new mesh, losing some accuracy as a result.

#### ALE

 An alternative to this approach is to use ALE which is, sad to say, an acronym for Arbitrary-Lagrangian-Eulerian. The node points are advected but not at the same rate as the flow. This can be used to prevent mesh tangling while still mitigating the worst difficulties associated with the advection term. But, on the other hand, it hasn't entirely eliminated that term.

#### DLR

 A different method is to start with an optimal, Delaunay, triangulation and allow the grid points to move locked into the fluid so as to eliminate the convection term from the differential equation. The mesh connections are checked at each timestep to see if the triangulation is still optimal. From near-optimal to optimal in this way involves exchanging a few node connections. This continual updating avoids ever being in a situation where full remeshing is required and thus avoids the loss of information during that process. Additional nodes can be introduced to improve resolution where required. The disadvantage of this procedure is in tracking history variables such as stress rate. These are only defined on the element interiors not the nodes, so the result is the tracking of a somewhat smoothed quantity. (brought to you by the Natural Element people)




<!-- ### References

...  -->
