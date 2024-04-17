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
            Predict();
        }

        catch (PythonException ex)
        {
            System.Console.WriteLine("Erro ao executar o arquivo Python" + ex.Message);
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
            dynamic model = tf.keras.models.load_model("modelao");
            dynamic list = new PyList();
            list.append(tf.keras.utils.load_img("imagemteste"));
            dynamic data = np.array(list);
            dynamic result = model.predict(data);
            Console.WriteLine(result);
        }
        catch (PythonException ex)
        {
            System.Console.WriteLine("Falha ao tentar executar o modelo" + ex.Message);
        }
    }
}


