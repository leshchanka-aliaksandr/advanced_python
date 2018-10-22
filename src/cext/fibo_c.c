#include <Python.h>



int fib(int n){
    int a = 1, b = 1, i = 1;
    while (i != n) {
        int tmp = a;
        a = b;
        b = tmp + b;
        i++;
    }
    return a;

}



static PyObject* fibo(PyObject* self, PyObject* args) {

  int n = 2;

  PyArg_ParseTuple(args, "i", &n);

  return Py_BuildValue("i", fib(n));

}



static PyMethodDef fib_count_funcs[] = {

  {"fibo",

   (PyCFunction)fibo,

   METH_VARARGS,

   "Counts fibonacci n'th element"},

   {NULL, NULL, 0, NULL}

};



static struct PyModuleDef moduledef = {

  PyModuleDef_HEAD_INIT,

  "fib_count_c",

  NULL,

  -1,

  fib_count_funcs

};



PyMODINIT_FUNC  PyInit_fib_count_c(void) {

  return PyModule_Create(&moduledef);

}