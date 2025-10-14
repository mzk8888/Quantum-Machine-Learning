
-----------------------------README-----------------------------------------

All the codes have been tested successfully at the Google Colab environment. 
However, since we are using qiskit, there is no guarantee that all the codes 
uploaded here will work properly because the version of qiskit is changed frequently.
However, by specifying the correct version of the code as shown in Attention~1, 
most of the code will execute properly.



-----------------------------ATTENTION~1-----------------------------------------

1.  pip install qiskit[visualization]==0.44.1
2.  pip install qiskit-aer==0.12.2

-----------------------------ATTENTION~1-----------------------------------------

     .
    
     .

In case the above method is not working properly, please follow the suggestions
listed in Attention~2 to tackle the issue. I apologize for the inconvenience.

-----------------------------ATTENTION~2-----------------------------------------

1.  please use 'from qiskit_aer import AerSimulator' if you want 
to use ' Aer' as backend.

2.  In case the 'execute' is not working, and there shows error like ' excecute is not defined'
please use transpile and assemble separately:

     transpiled_qc = transpile(qc, simulator)

     qobj = assemble(transpiled_qc)

     result = simulator.run(qobj).result()

-----------------------------ATTENTION~2-----------------------------------------
