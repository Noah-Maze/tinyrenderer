defmodule Rend do
  def addLine(start,stop) when abs(elem(start,0)-elem(stop,0) + elem(start,1)-elem(stop,1))<=1 do
    IO.puts(abs(elem(start,0)-elem(stop,0)) + (elem(start,1)-elem(stop,1)))
    IO.puts(abs(elem(start,0)-elem(stop,0)) + (elem(start,1)-elem(stop,1))<=1)
    [start, stop]
    end
  def addLine(start, stop) do
    [addLine(start, {Float.floor((elem(start,0)+elem(stop,0))/2), Float.floor((elem(start,1)+elem(stop,1))/2)}) |
     addLine({Float.ceil((elem(start,0)+elem(stop,0))/2), Float.ceil((elem(start,1)+elem(stop,1))/2)}, stop)]
    end
  end


#pixel_data = [[[0xFF,0xFF,0xFF],[0x00,0x00,0x00]],[[0x00,0x00,0x00],[0xFF,0xFF,0xFF]]]
#Bump.write(filename: "output/file.bmp", pixel_data: pixel_data)
#pixel_data = Bump.pixel_data("output/file.bmp")

#canvas = Canvas.size(%Size{height: 400, width: 400}) |>
#        Canvas.fill(color: Color.named(:red))

#Bump.write(filename: "output/red.bmp", canvas: canvas)
#canvas2 = Canvas.fill(canvas, color: Color.named(:blue),
#                   rect: %Rect{ size: %Size{height: 200, width: 200},
#                 origin: %Point{x: 100, y: 100}})
#Bump.write(filename: "output/redblue.bmp", canvas: canvas2)
start = {0,0}
stop = {1,1}
IP.puts(Rend.addLine(start, stop)
