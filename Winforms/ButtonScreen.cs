using System.Drawing;
using System.Windows.Forms;

public class ButtonScreen : ScreenObject
{
    public ButtonScreen(string name, float x, float y, float width, float height)
        : base(name, x, y, width, height)
    {

    }

    public ButtonScreen(string name, float x, float y, string path)
        : base(name, x, y, path)
    {

    }
}