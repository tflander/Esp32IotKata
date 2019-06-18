Let's do an exercise that is a big part of what we do as professional software engineers.  We take cryptic (crappy) code that is difficult to understand and difficult to extend, and we clean it.

The truth is that I was tired of MicroPython spikes and learning Python TDD, and wanted to cobble together a working solution for the phonebooth in-use detector.  Since this is a pretty simple problem, I could probably get away with releasing crappy code.  Imagine this detector was just one part of a factory automation problem.  Imagine we needed the ability to extend the code for new machines, new lines, and product change-over.  Imagine my 100 line crappy program was now 10,000 lines of crappy code.  Imagine I needed to train someone to maintain 10,000 lines of crappy code.  Imagine the plant manager expected that we were able to make changes quickly and safely.

I'll put my solution in the solutions folder, but you may end up with something quite different.  Make sure you don't break the code as you clean and test protect it.

I may defer test protecting the picoweb code.  We will see what happens.
