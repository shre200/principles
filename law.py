 #Import necessary libraries
import streamlit as st

# Function to explain physics laws
def explain_law(law_name):
    if law_name == "Newton's 1st Laws":
        st.title("NEWTONS 1ST LAW")
        st.write("Newton's First Law: An object at rest stays at rest, and an object in motion stays in motion with the same speed and in the same direction unless acted upon by an external force.")
        st.write("FORMULA: F=0 when there is no external force")
        st.write("EXAMPLES: a book is resting on a table will remain at rest unless a force is applied to move")
        st.image('1stlaw.gif')
        st.image('new.jpg')
    elif law_name =="newtons 2nd law":
        st.title("NEWTONS 2ND LAW")
        st.write("Newton's Second Law: The force acting on an object is equal to the mass of that object multiplied by its acceleration.")
        st.write("FORMULA: F=ma")
        st.write("SI unit= NEWTONS")
        st.write("EXAMPLES: if you apply a force to a sled it will accelerate more if it has less mass")
        st.image('2ndlaw.webp')
        st.image('2.gif')
        st.image('2@.gif')
    elif law_name =="newtons 3rd law":
        st.title("NEWTONS 3RD LAW")
        st.write("Newton's Third Law: For every action, there is an equal and opposite reaction.")
        st.write("FORMULA: F=-F")
        st.write("EXAMPLES: as you swim, you push the water backward with your arms and legs and the water pushes you forward")
        st.image('3rdlaw.gif')
        st.image('new2.webp')
    elif law_name == "Ohm's Law":
        st.title("OHMS LAW")
        st.write("STATEMENTS: The current passing through a conductor between two points is directly proportional to the voltage across the two points.")
        st.write("FORMULA: V=I*R")
        st.write("where v=voltage in volts")
        st.write("I=current in amperes")
        st.write("R=resistance in ohms")
        st.write("SI UNIT: ohms")
        st.write("EXAMPLES:if you have a circuit with a voltage of 12 volts (( V = 12V )) and a resistance of 4 ohms (( R = 4\Omega )), you can find the current (( I )) by rearranging Ohm's Law:I=V/R = 12v/4 ohms = 3 amperes")
        st.image('ohm.gif')
    elif law_name == "pauli exclusion principle":
        st.title("PAULIs EXCLUSION PRINCIPLES")
        st.write("STATEMENTS:no two electrons will have an identical set or the same quantum numbers (n, l, m, and s).")
        st.write("EXAMPLES: in a helium atom, the atom has 2 bound electrons and they occupy the outermost shell with opposite spins. ")
        st.image('pau.png')
        st.image('p.png')
        st.image('sp.gif')
    elif law_name == "pascals law":
        st.title("PASCALS LAW")
        st.write("STATEMENTS:The external static pressure applied on a confined liquid is distributed or transmitted evenly throughout the liquid in all directions.")
        st.write("APPLICATIONS:Hydraulic machines such as hydraulic press, hydraulic brakes, and hydraulic jacks ")
        st.write("SI UNIT:Pascals")
        st.image('q3.png')
        st.image('pas2.gif')
        st.image('pas.gif')
    elif law_name == "biot savarts law":
        st.title("BIOT SAVARTS LAW")
        st.write(" STATEMENTS:magnetic field due to a current-carrying conductor at a distance point is inversely proportional to the square of the distance between the conductor and point, and the magnetic field is directly proportional to the length of the conductor, current flowing in the conductor")
        st.write("APPLICATIONS: To calculate the magnetic field in the centre of a current-carrying arc, To calculate the force between two parallel and lengthy current-carrying conductors, To calculate the magnetic field along the axis of a circular current-carrying coil.")
        st.image('b.jpg')
        st.image('bio.png')
    elif law_name == "coulombs law":
        st.title("COULOMBS LAW")
        st.write("STATEMENTS:a law stating that like charges repel and opposite charges attract, with a force proportional to the product of the charges and inversely proportional to the square of the distance between them.")
        st.write("F	= 	electric for ",
                 "q_1, q_2	= 	charges",
                 " r	= 	distance of separation"
                 "k= coulombs constant")
        st.image('q2.jpg')
        st.image('q1.jpg')
    elif law_name == "newtons law of cooling":
        st.title("NEWTONS LAW OF COOLING")
        st.write(" ACCORDING TO NEWTONS LAW OF COOLING,: the rate of loss of heat from a body is directly proportional to the difference in the temperature of the body and its surroundings.")
        st.write("APPLICATIONS:To predict how long it takes for a hot object to cool down at a certain temperature.To find the temperature of a soda placed in a refrigerator by a certain amount of time.It helps to indicate the time of death given the probable body temperature at the time of death and current body temperature.")
        st.image("nc.png")
        st.image("nc2.jpg")
    elif law_name == "keplers law":
        st.title("KEPLERS LAW")
        st.write("KEPLER`S FIRST LAW,: “All the planets revolve around the sun in elliptical orbits having the sun at one of the foci”. The point at which the planet is close to the sun is known as perihelion (about 147 million kilometres from the sun), and the point at which the planet is farther from the sun is known as aphelion (152 million kilometres from the sun). It is characteristic of an ellipse that the sum of the distances of any planet from two foci is constant.")
        st.write("KEPLER`S SECOND LAW,: “The radius vector drawn from the sun to the planet sweeps out equal areas in equal intervals of time”.")
        st.write("KEPLER`S THIRD LAW,:”The square of the time period of revolution of a planet around the sun in an elliptical orbit is directly proportional to the cube of its semi-major axis”.T2 ∝ a3 The shorter the orbit of the planet around the sun, the shorter the time taken to complete one revolution. Using the equations of Newton’s law of gravitation and laws of motion, Kepler’s third law takes a more general form.")
        st.image('kep.gif')
        st.image('kep#2.gif')
        st.image('kep3.jpg')
        st.image('ke.jpg')
    elif law_name == "law of thermodynamics":
        st.title("LAWS OF THERMODYNAMICS")
        st.write( "1ST LAW OF THERMODYNAMICS,:energy cannot be created or destroyed. Alternatively, some sum it up as the conservation of energy. Ultimately, the First Law of Thermodynamics is a statement that energy can be transferred between the system and the surroundings through the transfer of heat (q) or by the performance of mechanical work (w).")
        st.image('T1.gif')
        st.write("2ND LAW OF THERMODYNAMICS:The Second Law of Thermodynamics can be stated in any of three synonymous ways:For a spontaneous process, the entropy of the universe increases.For a spontaneous process,  ΔSuniverse > 0. For a spontaneous process, ΔS system + ΔSsurroundings > 0 ΔE =q + w"
                 "The last statement of the Second Law of Thermodynamics divides the universe into two parts: the system (what you're investigating) and the surroundings (everything in the universe besides the system).  In chemistry the system is often a chemical reaction under investigation.  To be clear the Second Law does NOT mean that ΔSreaction must be positive as ΔSreaction is just the ΔSsystem which can be either positive or negative.  But if ΔSreaction for a spontaneous reaction is negative, then the Second Law does mean that ΔSsurroundings must be positive and of greater magnitude in this example so that ΔSsystem + ΔSsurroundings > 0.")
        st.image('T0.gif')
        st.write("3RD LAW OF THERMODYNAMICS:The Third Law of Thermodynamics states that a perfect crystal at zero Kelvin (absolute zero) has zero entropy.  First, a perfect crystal means that there are no impurities, has achieved thermodynamic equilibrium, and that it is in a crystalline state where all the atoms/ion/molecules are in well-defined positions in a highly-ordered crystalline lattice.  This would exclude amorphous solids like glass that don't have an ordered, crystalline structure and have not achieved thermodynamic equilibrium.")
        st.image('T3.png')
        st.image('ALLT.png')

def main():
    st.title("PRINCIPLES AND LAWs")
    st.header("",divider='rainbow')
    law_name = st.sidebar.selectbox("SELECT LAWS OR PRINCIPLES:", ["Newton's 1st Laws","newtons 2nd law","newtons 3rd law","Ohm's Law","pauli exclusion principle","pascals law","biot savarts law","coulombs law","newtons law of cooling","keplers law","law of thermodynamics"])
    explain_law(law_name)

# Run the app
if __name__ == "__main__":
    main()