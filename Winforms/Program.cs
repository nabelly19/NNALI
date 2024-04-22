using System;
using System.Windows.Forms;
using Python.Runtime;

// try
// {
//     Pythonet py = new Pythonet(
//         "python311.dll",
//         "neuralnet\\checkpoints\\good_model\\model9292(95ms).keras"
//     );

//     py.Initialize();
//     py.Predict();
// }
// catch (Exception ex)
// {
//     MessageBox.Show(ex.Message);
// }
ApplicationConfiguration.Initialize();

Application.Run(new WhiteBoard());


// using System;
// using System.IO;
// using System.Windows.Forms;
// using Python.Runtime;

// try
// {
//     // dotnet add package pythonnet

//     // python --version
//     Runtime.PythonDLL = "python311.dll";
//     PythonEngine.Initialize();
//     dynamic tf = Py.Import("tensorflow");
//     dynamic np = Py.Import("numpy");
//     MessageBox.Show(Directory.GetCurrentDirectory());
//     MessageBox.Show("4");
//     // Adiciona o diretório "src" ao caminho de busca do Python
//     // Importa o módulo predict.py
//     dynamic predictModule = Py.Import("src/predict.py");
//     MessageBox.Show("5");
//     dynamic model = tf.keras.models.load_model("neuralnet\\checkpoints\\good_model\\model9292(95ms).keras");
//     MessageBox.Show("6");
//     string result = predictModule.run("winforms\\FPS_0.png", model);
//     MessageBox.Show("7");
//     MessageBox.Show(result);
//     PythonEngine.Shutdown();
// }
// catch (Exception ex)
// {
//     PythonEngine.Shutdown();
//     MessageBox.Show(ex.Message);
// }
// ApplicationConfiguration.Initialize();

// Application.Run(new WhiteBoard());

