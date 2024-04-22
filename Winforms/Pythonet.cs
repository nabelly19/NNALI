using System;
using System.CodeDom.Compiler;
using System.Windows.Forms;
using Python.Runtime;

namespace Python.Runtime;

public class Pythonet 
{
    private string _pythonDLLPath;
    private string _modelName;

    public Pythonet(string pythonDLLPath, string modelName)
    {
        this._pythonDLLPath = pythonDLLPath;
        this._modelName = modelName;
    } 

    public void Initialize()
    {
        try
        {
            Runtime.PythonDLL = _pythonDLLPath;
            PythonEngine.Initialize();
        }

        catch (PythonException ex)
        {
            MessageBox.Show("Erro ao executar o arquivo Python" + ex.Message);
        }
        finally
        {
            PythonEngine.Shutdown();
        }
    }

    public void Predict()
    {
        try 
        {
            dynamic tf = Py.Import("tensorflow");
            dynamic np = Py.Import("numpy");
            dynamic predictModule = Py.Import("src\\predict.py");

            dynamic model = tf.keras.models.load_model(this._modelName);
            string result = predictModule.run("winforms\\FPS_0.png", model);
            MessageBox.Show(result);
        }
        catch (PythonException ex)
        {
            MessageBox.Show("Falha ao tentar executar o modelo" + ex.Message);
        }
    }
}


