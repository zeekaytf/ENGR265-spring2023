import numpy as np
import os
import math
import sys


def parse_tensile_file(path_to_file):
    file = open(path_to_file)
    # required meta-data
    gage_diameter = -1
    maximum_force = - 1
    maximum_strain = -1
    # determine when to begin reading into these files
    begin_reading = False
    time = []
    displacement = []
    force = []
    strain = []
    # begin iterating through file
    for line in file:
        if line == '' or line == '\n':
            continue

        splits = line.strip().split(",")

        if begin_reading == False:

            # gather various meta data
            if splits[0] == "Gage Diameter":
                cleaned = splits[2].replace('\"', '')
                gage_diameter = float(cleaned)
            if splits[0] == "Maximum Force":
                cleaned = splits[2].replace('\"', '')
                maximum_force = float(cleaned)
            if splits[0] == "Maximum Strain":
                cleaned = splits[2].replace('\"', '')
                maximum_strain = float(cleaned)

        else:
            # parse the actual data
            time.append(float(splits[0].replace('\"', '')))
            displacement.append(float(splits[1].replace('\"', '')))
            force.append(float(splits[2].replace('\"', '')))
            strain.append(float(splits[3].replace('\"', '')))

        # try to find start of data
        if splits[0] == "(s)":
            begin_reading = True
    file.close()

    return gage_diameter, np.asarray(time), np.asarray(displacement), np.asarray(force), np.asarray(strain)


def calculate_stress(force, sample_diameter):
    """
    Calculate the stress (MPa) experienced by the test given a series of forces/loads (kN) and
    a sample diameter (mm)
    :param force: An array of forces/loads applied to the sample in Kilo Newtons (kN)
    :param sample_diameter: The diameter of the sample in millimeters (mm)
    :return: An array of stresses experienced by the sample in Kilo Pascals (KPa)
    """

    ### YOUR SOLUTION FROM STEP 1 TEMPLATE HERE ###

    return None


def calculate_max_strength_strain(strain, stress):
    """
    Calculate the Ultimate Tensile Stress and Fracture Strain
    :param strain: An array of Strain data (MPa)
    :param stress: An array of Strain data
    :return:
    Ultimate Tensile Stress: the maximum stress experienced
    Fracture Strain: the maximum strain experienced before fracture
    """

    ### YOUR SOLUTION FROM STEP 2 TEMPLATE HERE ###

    return -1, -1

def calculate_elastic_modulus(strain, stress):
    """
        Given a set of stress strain data, use the Secant Modulus at 40% method to determine
        the elastic modulus
        :param strain:
        :param stress:
        :return:
        linear_index: the index within the strain/stress data that is the end of the linear region
        slope: the slope for the linear region of the strain/stress data
        intercept: y-intercept for linear region best fit of strain/stress data
    """

    # dummy variables the function should over write
    linear_index = None
    slope = None
    intercept = None

    ### YOUR SOLUTION FROM STEP 3 TEMPLATE HERE ###

    return linear_index, slope, intercept

def calculate_percent_offset(slope, strain, stress):
    """
    Determine the 0.2% Offset Yield by identifying the intercept with the stress curve and a parallel line

    :param slope: Slope of the offset line. This should be the elastic modulus
    :param strain: An array of Strain data (MPa)
    :param stress: An array of Stress data
    :return:
    offset_line: the y-values for the 0.2% offset line
    intercept_index: The index where the offset line and the strain line intersect
    """
    # set the desired offset for the line
    offset = 0.002

    # calculate the offset line: y=m(x-0.002) + 0
    offset_line = None

    # measure distance from all points on graph to this line. Consider using the
    # abs() method to ensure values are positive
    distance = None

    # use argmin to find the index where the distance is minimal
    intercept_index = -1

    return offset_line, intercept_index

if __name__ == "__main__":
    import matplotlib.pyplot as plt

    # modify this line to select different materials/folders within tensile/
    material_folder = "1045CR"

    # modify this line to select different samples in the material folder
    sample_name = "C01A1045CR_1"


    ### Do not modify below this line ###

    path_to_directory = "../../../data/tensile/"
    path_to_samples = path_to_directory + material_folder + "/"

    # manually parse file to get gage diameter and then calculate cross-sectional area
    path_to_file = path_to_samples + sample_name + ".csv"

    # Step #1: Parse the file ane return based values
    # sample diameter (mm), time (s), displacement (mm), force (kN), and strain (%)
    sample_diameter, time, displacement, force, strain = parse_tensile_file(path_to_file)

    # Step #1: Given the forces and sample diameter, calculate the strain
    stress = calculate_stress(force, sample_diameter)

    if stress is None:
        print("Error! No stress returned. Did you fill in the calculate_stress() method?")
        sys.exit(-1)

    # use scatter plot so we don't assume a line (yet)
    plt.scatter(strain, stress, label="Stress - Strain")
    plt.xlabel('Strain (mm/mm)')
    plt.ylabel('Stress (MPa)')
    plt.title('Stress-Strain Curve for Sample ' + sample_name)
    plt.show()

    # Step #2: Calculate basic parameters such as the ultimate tensile strength
    # and fracture strain

    # calculate easy variables
    ultimate_tensile_strength, fracture_strain = calculate_max_strength_strain(strain, stress)

    if ultimate_tensile_strength==-1 or fracture_strain ==-1:
        print("Error! Tensile Strength or Fracture Strain returned as -1. Did you complete the calculate_max_strength() method?")
        sys.exit(-1)

    print("Ultimate Tensile Stress is ", ultimate_tensile_strength, "MPa")
    print("Fracture Strain is ", 100 * fracture_strain, " percent")

    # Step #3: Use the Secant Modulus at 40% of Peak Strain
    # to determine elastic modulus

    linear_index, slope, intercept = calculate_elastic_modulus(strain, stress)

    if linear_index is None or slope is None or intercept is None:
        print("Incorrect value determined by calculate_elastic_modulus() did you implement that function?")
        sys.exit(-1)

    print("Elastic Modulus is ", slope / 1000, 'GPa')

    # show the original curve indicating the secant modulus at 40%
    plt.scatter(strain, stress, label="Stress - Strain")
    plt.xlabel('Strain (mm/mm)')
    plt.ylabel('Stress (MPa)')
    plt.title('Stress-Strain Curve for Sample ' + sample_name)

    plt.scatter(strain[linear_index], stress[linear_index], marker="v", label="Secant Modulus at 40%")

    plt.legend()
    plt.show()

    # now plot the linear region for the best fit line
    linear_strain = strain[0:linear_index]
    linear_stress = stress[0:linear_index]

    plt.scatter(linear_strain, linear_stress, label="Stress - Strain")
    plt.xlabel('Strain (mm/mm)')
    plt.ylabel('Stress (MPa)')
    plt.title('Linear Region for Sample ' + sample_name + ' with best fit')

    # compute line y=mx+b
    best_fit_line = slope * linear_strain + intercept
    plt.plot(linear_strain, best_fit_line, label="Best Linear Fit")

    plt.legend()
    plt.show()

    ### Step 4: calculate 0.2% yield strength ###
    offset_line, intercept_index = calculate_percent_offset(slope, strain, stress)

    if offset_line is None or intercept_index==-1:
        print("Calculate Percent Offset Returned None or -1. Did you return the correct values?")
        sys.exit(-1)

    # print out the results
    print("The 0.2% Offset Yield is ", stress[intercept_index], " MPa")

    # create line parallel to linear region and find intersection with overall curve
    plt.scatter(strain, stress, label="Stress - Strain")
    plt.xlabel('Strain (mm/mm)')
    plt.ylabel('Stress (MPa)')
    plt.title('Stress-Strain Curve for Sample ' + sample_name + " with 0.2% Yield")

    # plot yield line
    plt.plot(strain, offset_line, label="0.2% Offset Yield")

    # indicate point where yield intersects
    plt.plot(strain[intercept_index], stress[intercept_index], marker='v', label="Yield Strength")

    # since this will go on forever, constrain the axis
    plt.xlim([-.001, max(strain)])
    plt.ylim([0, 1.1 * max(stress)])
    plt.legend()
    plt.show()

    print("Done!")



