# Superpose.py - Quickly superpose all molecules in Coot on a reference structure.
# Written by Sakib Hossain - 08/16/18

global_ref = []

if (have_coot_python):
    if coot_python.main_menubar():
        menu = coot_menubar_menu("Superpose")

        def reference_structure(imol1):
            ref = int(imol1)
            global_ref.insert(0, ref)
            return ref

        def superposition():
            for i in range(len(molecule_number_list())):
                superpose(int(global_ref[0]), i, 0)

        add_simple_coot_menu_menuitem(
            menu,
            "Choose Reference Structure",
            lambda func:
            molecule_chooser_gui("Reference Molecule: ",
                             lambda reference:
                             reference_structure(reference)))

        add_simple_coot_menu_menuitem(
            menu,
            "Start Superpose",
            lambda func:
            superposition()
            )