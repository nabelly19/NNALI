using System;
using System.Collections.Generic;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Windows.Forms;

public partial class WhiteBoard : Form
{
    public static List<ScreenObject> Objs { get; private set; } = new();
    public static void AddObject(ScreenObject obj) => Objs.Add(obj);
    private PictureBox pb = new PictureBox { Dock = DockStyle.Fill };
    private Graphics g = null;
    private Bitmap b = null;
    private Timer t;
    private Point previousPoint;
    private bool drawing = false;
    private bool eraserMode = false;
    private int frameCounter = 0;
    private int penSize = 20;
    private Brush brush = new SolidBrush(Color.Black);
    private Stack<Bitmap> undoStack = new Stack<Bitmap>(); 
    private Button btnSaveThis = new Button { Text = "Save Next", Dock = DockStyle.Bottom, BackColor = Color.White };
    private Button btnDraw = new Button {Text = "Pen", Dock = DockStyle.Left, Width = 20, Height = 20, BackColor = Color.White};
    private Button btnEraser = new Button {Text = "Eraser", Dock = DockStyle.Left, Width = 20, Height = 20, BackColor = Color.White};
    private Button btnIncreasePenSize = new Button {Text = "+", Dock = DockStyle.Right, Width = 20, Height = 20, BackColor = Color.White};
    private Button btnDecreasePenSize = new Button {Text = "-", Dock = DockStyle.Right, Width = 20, Height = 20, BackColor = Color.White};
    private TextBox txb = new TextBox
    {
        Dock = DockStyle.Top,
        Multiline = true,
        Height = 150,
        Font = new Font("Roboto", 42),
    };

    public WhiteBoard()
    {
        WindowState = FormWindowState.Maximized;
        FormBorderStyle = FormBorderStyle.None;

        b = new Bitmap(pb.Width, pb.Height);
        pb.Image = b;
        t = new Timer { Interval = 10 };

        Load += Form_Load;

        this.KeyPreview = true;
        this.KeyDown += KeyboardDown;

        Controls.Add(this.pb);
        Controls.Add(this.btnSaveThis);
        Controls.Add(this.btnDecreasePenSize);
        Controls.Add(this.btnIncreasePenSize);
        Controls.Add(this.btnDraw);
        Controls.Add(this.btnEraser);
        Controls.Add(this.txb);

        this.btnSaveThis.Click += ThisBtnToSave;

        this.btnDraw.Click += (sender, e) =>
        {
            MessageBox.Show("tá lápis");
            eraserMode = false;
            brush = new SolidBrush(Color.Black);
        };

        this.btnEraser.Click += (sender, e) =>
        {
            MessageBox.Show("tá borracha");
            eraserMode = true;
            brush = new SolidBrush(Color.White);
        };

        this.btnIncreasePenSize.Click += (sender, e) =>
        {
            if (penSize < 45)
                penSize += 5;
            else 
                MessageBox.Show("Limite máximo da espessura da caneta atingido");
        };

        this.btnDecreasePenSize.Click += (sender, e) =>
        {
            if (penSize > 6)
                penSize-= 5;
            else 
                MessageBox.Show("Limite mínimo da espessura da caneta atingido");
                return;
        };
 
        this.pb.MouseDown += (sender, e) =>
        {
            

            if (e.Button == MouseButtons.Left)
            {
                AddStateToUndoStack();
                drawing = true;
                previousPoint = e.Location;
            }
        };

        this.pb.MouseMove += (sender, e) =>
        {
            if (drawing)
            {
                var deltaX = e.X - previousPoint.X;
                var deltaY = e.Y - previousPoint.Y;
                var distancia = Math.Sqrt(Math.Pow(deltaX, 2) + Math.Pow(deltaY, 2));
                for (float i = 0; i < 1; i += 1f / (float)distancia)
                {
                    var x = (1 - i) * previousPoint.X + i * e.X;
                    var y = (1 - i) * previousPoint.Y + i * e.Y;
                    g.FillEllipse(brush,
                        x - penSize / 2,
                        y - penSize / 2,
                        penSize, penSize);
                }
                pb.Refresh();
                previousPoint = e.Location;
            }
        };

        this.pb.MouseUp += (sender, e) =>
        {
            if (e.Button == MouseButtons.Left)
            {
                drawing = false;
            }
        };

        Text = "Testing...";
    }

    private void Form_Load(object sender, EventArgs e)
    {
        this.b = new Bitmap(pb.Width, pb.Height);

        this.g = Graphics.FromImage(this.b);
        this.g.InterpolationMode = InterpolationMode.NearestNeighbor;
        this.g.Clear(Color.White);
        this.pb.Image = b;
        this.t.Start();
        AddObject(new ButtonScreen("teste", pb.Width/2, pb.Height/2,"obj.png"));
    }

    private void KeyboardDown(object sender, KeyEventArgs e)
    {
        switch (e.KeyCode)
        {
            case Keys.Escape:
                Application.Exit();
                break;
            case Keys.P:
                DownloadNextFrame();
                break;
        }

         if (e.KeyCode == Keys.E)
            {
                eraserMode = !eraserMode;
                this.brush = eraserMode ? new SolidBrush(Color.White) : new SolidBrush(Color.Black);
            }

        if (e.KeyCode == Keys.Up)
            penSize ++;
        if (e.KeyCode == Keys.Down)
            penSize --;

        if (e.KeyCode == Keys.ControlKey && e.KeyCode == Keys.Z)
            CtrlZ();
    }

    private void AddStateToUndoStack()
    {
        Bitmap crrState = new Bitmap(this.b);
        undoStack.Push(crrState);
    }

    private void CtrlZ()
    {
        if (undoStack.Count > 0)
        {
            b = undoStack.Pop();
            g = Graphics.FromImage(this.b);
            pb.Image = b;
            pb.Refresh();
        }
        else 
            MessageBox.Show("Ação Impossível");
    }

    private void DownloadNextFrame()
    {
        Bitmap print = new Bitmap(this.Width, this.Height);
        this.DrawToBitmap(print, new Rectangle(0, 0, this.Width, this.Height));

        string printName = $"FPS_{frameCounter}.png";
        print.Save(printName, System.Drawing.Imaging.ImageFormat.Png);
        frameCounter++;
    }

    private void ThisBtnToSave(object sender, EventArgs e)
    {
        Bitmap print = new Bitmap(this.Width, this.Height);
        this.DrawToBitmap(print, new Rectangle(0, 0, this.Width, this.Height));

        string printName = $"FPS_{frameCounter}.png";
        print.Save(printName, System.Drawing.Imaging.ImageFormat.Png);
        frameCounter++;
    }
}
