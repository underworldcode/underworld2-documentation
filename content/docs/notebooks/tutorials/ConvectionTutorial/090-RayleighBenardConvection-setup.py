##
## As though you ran the whole 050-RayleighBenardNotebook setup cells 
##

import underworld as uw
from underworld import function as fn
import glucifer
import math
import numpy as np

# Set number of dimensions.
dim = 2

# Set simulation box size.
boxHeight = 1.0
boxLength = 2.0

# Set the resolution.
res = 16

# Set min/max temperatures.

tempMin = 0.0
tempMax = 1.0


# Create mesh and variables
# ------
# 
# The mesh object has both a primary and sub mesh. "Q1/dQ0" produces a primary mesh with element type Q1 and a sub-mesh with elements type dQ0. Q1 elements have node points at the element corners, dQ0 elements have a single node at the elements centre.


mesh = uw.mesh.FeMesh_Cartesian( elementType = ("Q1/dQ0"), 
                                 elementRes  = (int(boxLength*res), res), 
                                 minCoord    = (0., 0.), 
                                 maxCoord    = (boxLength, boxHeight))
Tmesh = mesh

# Create mesh variables.  Note the pressure field uses the sub-mesh, the temperature uses the same mesh at this stage. The `temperatureDotField` variable is a work array for the advection-diffusion solver.


velocityField       = uw.mesh.MeshVariable( mesh=mesh,         nodeDofCount=dim )
pressureField       = uw.mesh.MeshVariable( mesh=mesh.subMesh, nodeDofCount=1 )

temperatureField    = uw.mesh.MeshVariable( mesh=Tmesh,         nodeDofCount=1 )
temperatureDotField = uw.mesh.MeshVariable( mesh=Tmesh,         nodeDofCount=1 )

# Initialise values
velocityField.data[:]       = [0.,0.]
pressureField.data[:]       = 0.
temperatureDotField.data[:] = 0.

## These are for the exercise where the mesh resolution changes


mesh0 = uw.mesh.FeMesh_Cartesian( elementType = ("Q1/dQ0"), 
                                 elementRes  = (int(boxLength*8), 8), 
                                 minCoord    = (0., 0.), 
                                 maxCoord    = (boxLength, boxHeight))

mesh1 = uw.mesh.FeMesh_Cartesian( elementType = ("Q1/dQ0"), 
                                 elementRes  = (int(boxLength*16), 16), 
                                 minCoord    = (0., 0.), 
                                 maxCoord    = (boxLength, boxHeight))

mesh2 = uw.mesh.FeMesh_Cartesian( elementType = ("Q1/dQ0"), 
                                 elementRes  = (int(boxLength*32), 32), 
                                 minCoord    = (0., 0.), 
                                 maxCoord    = (boxLength, boxHeight))


Tmesh0 = mesh0
Tmesh1 = mesh1
Tmesh2 = mesh2

velocityField0       = uw.mesh.MeshVariable( mesh=mesh0,          nodeDofCount=dim )
velocityField1       = uw.mesh.MeshVariable( mesh=mesh1,          nodeDofCount=dim )
velocityField2       = uw.mesh.MeshVariable( mesh=mesh2,          nodeDofCount=dim )

pressureField0       = uw.mesh.MeshVariable( mesh=mesh0.subMesh,  nodeDofCount=1 )
pressureField1       = uw.mesh.MeshVariable( mesh=mesh1.subMesh,  nodeDofCount=1 )
pressureField2       = uw.mesh.MeshVariable( mesh=mesh2.subMesh,  nodeDofCount=1 )

temperatureField0    = uw.mesh.MeshVariable( mesh=Tmesh0,         nodeDofCount=1 )
temperatureField1    = uw.mesh.MeshVariable( mesh=Tmesh1,         nodeDofCount=1 )
temperatureField2    = uw.mesh.MeshVariable( mesh=Tmesh2,         nodeDofCount=1 )

temperatureDotField0 = uw.mesh.MeshVariable( mesh=Tmesh0,         nodeDofCount=1 )
temperatureDotField1 = uw.mesh.MeshVariable( mesh=Tmesh1,         nodeDofCount=1 )
temperatureDotField2 = uw.mesh.MeshVariable( mesh=Tmesh2,         nodeDofCount=1 )


# Initialise values
velocityField0.data[:]       = [0.,0.]
velocityField1.data[:]       = [0.,0.]
velocityField2.data[:]       = [0.,0.]

pressureField0.data[:]       = 0.
pressureField1.data[:]       = 0.
pressureField2.data[:]       = 0.

temperatureDotField0.data[:] = 0.
temperatureDotField1.data[:] = 0.
temperatureDotField2.data[:] = 0.


# Set up material parameters and functions
# -----
# 
# Set functions for viscosity, density and buoyancy force. These functions and variables only need to be defined at the beginning of the simulation, not each timestep.


# Set viscosity to be a constant.
viscosity = 1.
Ra = 1.0e4

# Construct a density function.
densityFn = Ra * temperatureField

# Define our vertical (upward) unit vector using a python tuple (this will be automatically converted to a function).
z_hat = ( 0.0, 1.0 )

# Now create a buoyancy force vector using the density and the vertical unit vector. 
buoyancyFn = densityFn * z_hat


# Create initial & boundary conditions
# ----------
# 
# Set a sinusoidal perturbation in the temperature field to seed the onset of convection.
# 
# Set top and bottom wall temperature boundary values.


pertStrength = 0.2

deltaTemp = tempMax - tempMin

for index, coord in enumerate(Tmesh.data):
    pertCoeff = math.cos( math.pi * coord[0] ) * math.sin( math.pi * coord[1] )
    temperatureField.data[index] = tempMin + deltaTemp*(boxHeight - coord[1]) + pertStrength * pertCoeff
    temperatureField.data[index] = max(tempMin, min(tempMax, temperatureField.data[index]))

for index in Tmesh.specialSets["MinJ_VertexSet"]:
    temperatureField.data[index] = tempMax
    
for index in Tmesh.specialSets["MaxJ_VertexSet"]:
    temperatureField.data[index] = tempMin


## Also do this for mesh0 but not for 1,2
    
for index, coord in enumerate(Tmesh0.data):
    pertCoeff = math.cos( math.pi * coord[0] ) * math.sin( math.pi * coord[1] )
    temperatureField0.data[index] = tempMin + deltaTemp*(boxHeight - coord[1]) + pertStrength * pertCoeff
    temperatureField0.data[index] = max(tempMin, min(tempMax, temperatureField0.data[index]))

for index in Tmesh0.specialSets["MinJ_VertexSet"]:
    temperatureField0.data[index] = tempMax
    
for index in Tmesh0.specialSets["MaxJ_VertexSet"]:
    temperatureField0.data[index] = tempMin

   
# Velocity and Temperature boundary conditions

# 2D velocity vector can have two Dirichlet conditions on each vertex, 
# v_x is fixed on the iWalls (vertical), v_y is fixed on the jWalls (horizontal)

iWalls     = mesh.specialSets["MinI_VertexSet"] + mesh.specialSets["MaxI_VertexSet"]
jWalls     = mesh.specialSets["MinJ_VertexSet"] + mesh.specialSets["MaxJ_VertexSet"]
freeslipBC = uw.conditions.DirichletCondition( variable        = velocityField, 
                                               indexSetsPerDof = (iWalls, jWalls) )
                                                                                           
jTWalls    = Tmesh.specialSets["MinJ_VertexSet"] + Tmesh.specialSets["MaxJ_VertexSet"]
tempBC     = uw.conditions.DirichletCondition( variable        = temperatureField, 
                                               indexSetsPerDof = (jTWalls,) )

iWalls     =  mesh0.specialSets["MinI_VertexSet"] +  mesh0.specialSets["MaxI_VertexSet"]
jWalls     =  mesh0.specialSets["MinJ_VertexSet"] +  mesh0.specialSets["MaxJ_VertexSet"]
jTWalls    = Tmesh0.specialSets["MinJ_VertexSet"] + Tmesh0.specialSets["MaxJ_VertexSet"]

freeslipBC0 = uw.conditions.DirichletCondition( variable        = velocityField0, 
                                               indexSetsPerDof = (iWalls, jWalls) )
tempBC0     = uw.conditions.DirichletCondition( variable        = temperatureField0, 
                                               indexSetsPerDof = (jTWalls,) )

iWalls     =  mesh1.specialSets["MinI_VertexSet"] +  mesh1.specialSets["MaxI_VertexSet"]
jWalls     =  mesh1.specialSets["MinJ_VertexSet"] +  mesh1.specialSets["MaxJ_VertexSet"]
jTWalls    = Tmesh1.specialSets["MinJ_VertexSet"] + Tmesh1.specialSets["MaxJ_VertexSet"]

freeslipBC1 = uw.conditions.DirichletCondition( variable        = velocityField1, 
                                               indexSetsPerDof = (iWalls, jWalls) )
tempBC1     = uw.conditions.DirichletCondition( variable        = temperatureField1, 
                                               indexSetsPerDof = (jTWalls,) )


iWalls     =  mesh2.specialSets["MinI_VertexSet"] +  mesh2.specialSets["MaxI_VertexSet"]
jWalls     =  mesh2.specialSets["MinJ_VertexSet"] +  mesh2.specialSets["MaxJ_VertexSet"]
jTWalls    = Tmesh2.specialSets["MinJ_VertexSet"] + Tmesh2.specialSets["MaxJ_VertexSet"]

freeslipBC2 = uw.conditions.DirichletCondition( variable        = velocityField2, 
                                               indexSetsPerDof = (iWalls, jWalls) )
tempBC2     = uw.conditions.DirichletCondition( variable        = temperatureField2, 
                                               indexSetsPerDof = (jTWalls,) )




# System setup
# Set up a Stokes equation template and an advection diffusion template

stokes = uw.systems.Stokes( velocityField = velocityField, 
                            pressureField = pressureField,
                            conditions    = [freeslipBC,],
                            fn_viscosity  = viscosity, 
                            fn_bodyforce  = buoyancyFn )

# Implicit Stokes solver
solver = uw.systems.Solver( stokes )
solver.set_inner_method("mumps")
solver.set_penalty(1.0e7)

# advDiff uses an explicit / timestepping approach
advDiff = uw.systems.AdvectionDiffusion( phiField       = temperatureField, 
                                         phiDotField    = temperatureDotField, 
                                         velocityField  = velocityField, 
                                         fn_diffusivity = 1.0, 
                                         conditions     = [tempBC,] )




                                               
# System setup - mesh 0,1,2
# Set up a Stokes equation template and an advection diffusion template

stokes0 = uw.systems.Stokes( velocityField = velocityField0, 
                             pressureField = pressureField0,
                             conditions    = [freeslipBC0,],
                             fn_viscosity  = viscosity, 
                             fn_bodyforce  = buoyancyFn )
                                               
                                               

# Implicit Stokes solver
solver0 = uw.systems.Solver( stokes0 )
solver0.set_inner_method("mumps")
solver0.set_penalty(1.0e7)

# advDiff uses an explicit / timestepping approach
advDiff0 = uw.systems.AdvectionDiffusion( phiField       = temperatureField0, 
                                          phiDotField    = temperatureDotField0, 
                                          velocityField  = velocityField0, 
                                          fn_diffusivity = 1.0, 
                                          conditions     = [tempBC0,] )


stokes1 = uw.systems.Stokes( velocityField = velocityField1, 
                             pressureField = pressureField1,
                             conditions    = [freeslipBC1,],
                             fn_viscosity  = viscosity, 
                             fn_bodyforce  = buoyancyFn )
                                               
                                               

# Implicit Stokes solver
solver1 = uw.systems.Solver( stokes1 )
solver1.set_inner_method("mumps")
solver1.set_penalty(1.0e7)

# advDiff uses an explicit / timestepping approach
advDiff1 = uw.systems.AdvectionDiffusion( phiField       = temperatureField1, 
                                          phiDotField    = temperatureDotField1, 
                                          velocityField  = velocityField1, 
                                          fn_diffusivity = 1.0, 
                                          conditions     = [tempBC1,] )

                                              
stokes2 = uw.systems.Stokes( velocityField = velocityField2, 
                             pressureField = pressureField2,
                             conditions    = [freeslipBC2,],
                             fn_viscosity  = viscosity, 
                             fn_bodyforce  = buoyancyFn )
                                               
                                               

# Implicit Stokes solver
solver2 = uw.systems.Solver( stokes2 )
solver2.set_inner_method("mumps")
solver2.set_penalty(1.0e7)

# advDiff uses an explicit / timestepping approach
advDiff2 = uw.systems.AdvectionDiffusion( phiField       = temperatureField2, 
                                          phiDotField    = temperatureDotField2, 
                                          velocityField  = velocityField2, 
                                          fn_diffusivity = 1.0, 
                                          conditions     = [tempBC2,] )


                                              
                                               
                                               
                                               
                                               
                                               

