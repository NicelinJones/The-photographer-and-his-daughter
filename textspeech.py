from gtts import gTTS
import os
import time
txt=" Once upon a time, there was a photographer who lived in London.He was a excellent photographer and took many amazing pictures.One day,his daughter, Gloria was looking through her dad's photos.Gloria,who was the daughter of Paul, the photographer,said to her dad,Dad I also want to be a photographer like you.As the years passed, twenty years later,Gloria grew into a beautiful young woman. Just as expected,she became a photographer. One day she traveled to a resort in the Maldives.The Maldives is a beautiful Island with many resorts, and it's a very pleasant place. That morning,Gloria stepped out of her villa, sat on the swing, and enjoyed the calmness of the day. While she was enjoying the morning,she noticed a rare bird, a pelican, near the shore catching fish. Gloria quietly got off the swing and wentback into the villa without making any noise.She grabbed her camera and tried to take a picture of the pelican.She took several photos, but the bird kept moving, and the photos were unclear.Seeing the pelican wasn't cooperating, Gloria decided to move closer to the Bird.She slowly approached it and tied one of the pelican's leg with a rope to keep it in placeThen she tried to take a photo with the pelican, but the bird was still not cooperating. It kept moving, squawking and frustrating her. Gloria became tired and frustrated. She started yelling at the bird  in anger, but that didn't help.Frustrated,She dropped the camera and sat on the swing.Just then the phone rang. It was her dad calling. Gloria explained the difficulties she was having with the pelican.Her dad,paul, listened patiently and then said, Gloria, birds are living creature just like us. They can't speak to us.But they have feelings.if you show your anger they won't cooperate. Instead, try showing kindness. This time Gloria didn't show her angryness instead she went near the bird and untied the rope and she put some medicine in the birds leg. She spoke with the bird. And said sorry to the bird she allowed the bird to fly and she said, bye bye, she went back to her villa.Surprisingly after five miniutes later, the pelican flew back and perched on her shoulder. Gloria was overjoyed! Now the pelican was calm and cooperated with her.They took many beautiful pictures together, and the pelican and Gloria became friends.The Moral.In this story Gloria showed kindness and love toward the pelican and in return ,the bird responded with love.Even though it was difficult for the pelican to pose, it endured and cooperated with Gloria once she showed  kindness.This teaches us that when we show love and kindness to others,  even when they might irritate us, we can build strong, positive relationships.The love Beareth all things, Believeth all things, Hopeth all things, Endureth all things.1 corinthians 13:8. " 
lang="en"
x=gTTS(text=txt,lang=lang,slow=False)
x.save("welcome.mp3")
os.system("start welcome.mp3")







