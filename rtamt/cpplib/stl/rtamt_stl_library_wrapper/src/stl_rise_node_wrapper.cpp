#include <boost/python.hpp>
#include <boost/python/def.hpp>
#include <boost/python/module.hpp>
#include <boost/python/wrapper.hpp>

#include <rtamt_stl_library/stl_node.h>
#include <rtamt_stl_library/stl_rise_node.h>
#include <rtamt_stl_library/stl_sample.h>

using namespace boost::python;
using namespace stl_library;

BOOST_PYTHON_MODULE(stl_rise_node)
{
    class_<StlRiseNode, bases<StlNode> >("StlRiseNode")
        .def("update", &StlRiseNode::update)
        .def("addNewInput", static_cast<void (StlRiseNode::*)(Sample)>(&StlRiseNode::addNewInput))
    ;
}

