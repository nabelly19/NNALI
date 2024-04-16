using System.Drawing;
using System.Windows.Forms;

public abstract class ScreenObject 
{
    public string Name { get; set; }
    public float X { get; set; }
    public float Y { get; set; }
    public float Width { get; set; }
    public float Height { get; set; }
    public Image Sprite { get; set; }	


    public ScreenObject(string name, float x, float y, string sprite)
    {
        this.Name = name;
        this.X = x;
        this.Y = y;
        setImage(sprite);
        this.Width = this.Sprite.Width;
        this.Height = this.Sprite.Height;
    }

    public ScreenObject(string name, float x, float y, Image image)
    {
        this.Name = name;
        this.X = x;
        this.Y = y;
        this.Sprite = image;
        this.Width = this.Sprite.Width;
        this.Height = this.Sprite.Height;
    }

    public ScreenObject(string name, float x, float y, float width, float height)
    {
        this.Name = name;
        this.X = x;
        this.Y = y;
        this.Width = width;
        this.Height = height;
    }

    private void setImage(string pathImage)
        => this.Sprite = Bitmap.FromFile(pathImage); 
}