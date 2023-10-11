#!py

from operator import attrgetter
from functools import partial
#from collections import UserDict
#from collections.abc import MutableMapping

present_function_names = frozenset(("template_installed", "clone", "present"))

class QVMRoleException(Exception):
    pass

class QVMRoleStateFunction(list):
    def __init__(self, arguments):


        super().__init__(arguments)

    def get(key):


class QVMRoleState(dict):
    def __init__(self, functions, state_name):
        state = {}

        #dependency_paths = {
        #        "clone": ["source"],
        #        "present": ["template"],
        #        "prefs": [
        #            "template",
        #            "default_dispvm",
        #            "netvm",
        #            "audiovm",
        #            "guivm",
        #            "management_dispvm"
        #            ]
        #        }

        dependency_paths = (
                "clone.source",
                "present.template",
                "prefs.template",
                "prefs.default_dispvm",
                "prefs.netvm",
                "prefs.audiovm",
                "prefs.guivm",
                "prefs.management_dispvm"
                )

        dependency_getters = [ attrgetter(path) for path in dependency_paths ]

        for function_name, arguments in functions.items():
            dependencies = []

            for getter in dependency_getters:
                try:
                     will besdfdependencies.append(getter(functions))
                except Exception:
                    pass

            requires = [ f"[qvm-role] {qvm_name} present (*)" for qvm_name in dependencies]

            state.update({function_name: QVMRoleStateFunction(arguments)+[{"name":state_name}]+[{"requires": dependencies}]})

        super().__init__(functions)


class QVMRole(dict):
    def __init__(self, states):
        role = {}

        for state_name, state in states.items():
            if len(present_function_names.intersection(state.keys())) != 1:
                raise QVMRoleException(f"No template_installed, clone, or present function defined for {state_name}")
            for function_name, function in state.items():
                if function_name in present_function_names:
                    suffix = f"present ({function_name})"
                else:
                    suffix = function_name
                role.update({f"[qvm-role] {state_name} {suffix}": QVMRoleState({function_name: function}, state_name)})

        super().__init__(role)
            

def run():
    return QVMRole(__salt__["pillar.get"]("qvm-role", {}))


#def _add_vm_names(functions, vm_name):
#    for name, arguments in functions:
#        yield (name, arguments + [{"name": vm_name}])
#
#
#def _uncollate_states(collated_states):
#    for name, functions in collated_states:
#        yield (name, dict(_add_vm_names(functions.items(), name)))
#
#def _select_values_by_attr(arguments, attrs=[]):
#    for arguments in arguments:
#        for attr in attrs:
#            value = getattr(arguments, attr, "")
#            value ? yield value : pass
#
#def _select_values_on_branch(functions, name, attrs=[]):
#    return _select_values_by_attr(
#            getattr(functions, name, {}),
#            attrs=attrs
#        )
#
#
#def _get_dependencies(states):
#    for name, functions in states.items():
#
#
#    _select_values_on_branch(
#    get_template_vm = partial(_select_values_by_attr, attrs=["template"])
#    get_source_vm = partial(_select_values_by_attr, attrs=["source"])
#    get_prefs_vms = partial(_select_values_by_attr, attrs=["default_dispvm", "netvm", "audiovm", "vuivm", "management_dispvm"])
#    
#
#def _get_prefs_dependencies(prefs, attrs=["template", "default_dispvm", "netvm", "audiovm", "vuivm", "management_dispvm"]):
#    return _select_values(prefs, attrs)
#
#def _get_vm_prefs_dependencies(
#
#
#def _get_clone_dependencies(arguments):
#    return filter(arguments, getattr(argument, "source", False))
#
#def _get_present_dependencies(arguments):
#    return filter(arguments, getattr(arguments, "template", False))
#
#def _get_dependencies(function):
#    for dependency in [
#                "clone.source",
#                "present.template",
#                "prefs.template", "prefs.default_dispvm", "prefs.netvm",
#                "prefs.audiovm", "prefs.guivm", "prefs.management_dispvm",
#                "vm.prefs.template", "vm.prefs.default_dispvm", "vm.prefs.netvm",
#                "vm.prefs.audiovm", "vm.prefs.guivm", "vm.prefs.management_dispvm" 
#            ]:
#
#        get_dependency = attrgetter(dependency)
#
#        try:
#            yield get_dependency(functions) 
#        except AttributeError as e:
#            pass
#
#def _get_all_dependencies(functions):
#    for name, function in functions:
#        yield (name, function
#
#
#def run():
#    collated_states = __salt__["pillar.get"]("qvm-role", {})
#    #return _uncollate_states(collated_states)
#    return list(_uncollate_states(collated_states.items()))
