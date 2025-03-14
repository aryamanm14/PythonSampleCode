import pygame
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Farming Advisor")

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

font = pygame.font.SysFont(None, 36)

day = 1
max_days = 30
input_stage = 0
temperature = ""
weather = ""
soil_moisture = ""
advice = ""

button_width = 100
button_height = 50
button_x = width - button_width - 10
button_y = height - button_height - 10
exit_button_x = 10
exit_button_y = height - button_height - 10

advice_dict = {
    "hot": "Water the plants early in the morning or late evening.",
    "cold": "Protect the plants with covers or move them indoors.",
    "rainy": "Ensure proper drainage to prevent waterlogging.",
    "dry": "Increase irrigation frequency and mulch around plants.",
    "low_moisture": "Water the soil deeply and regularly.",
    "high_moisture": "Improve drainage and avoid overwatering."
}

def get_advice(temp, weather, moisture):
    if temp > 30:
        temp_advice = advice_dict["hot"]
    else:
        temp_advice = advice_dict["cold"]

    if weather == "rainy":
        weather_advice = advice_dict["rainy"]
    else:
        weather_advice = advice_dict["dry"]

    if moisture < 50:
        moisture_advice = advice_dict["low_moisture"]
    else:
        moisture_advice = advice_dict["high_moisture"]

    return f"Temperature: {temp_advice}\nWeather: {weather_advice}\nSoil Moisture: {moisture_advice}"

def draw_button(screen, msg, x, y, w, h, ic, ac):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1:
            return True
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))

    small_text = pygame.font.SysFont(None, 20)
    text_surf = small_text.render(msg, True, BLACK)
    text_rect = text_surf.get_rect(center=((x + (w / 2)), (y + (h / 2))))
    screen.blit(text_surf, text_rect)
    return False

running = True
while running:
    screen.fill(GREEN)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    day_text = font.render(f"Day #{day}", True, BLACK)
    screen.blit(day_text, (10, 10))

    if input_stage == 0:
        temperature = input("Enter Temperature: ")
        input_stage = 1
    elif input_stage == 1:
        weather = input("Enter Weather (rainy/dry): ")
        input_stage = 2
    elif input_stage == 2:
        soil_moisture = input("Enter Soil Moisture(0%-100%: ")
        try:
            temp_value = int(temperature)
            moisture_value = int(soil_moisture)
            advice = get_advice(temp_value, weather, moisture_value)
        except ValueError:
            advice = "Invalid input. Please enter numeric values for temperature and soil moisture."
        input_stage = 3

    
    if input_stage == 3:
        advice_lines = advice.split('\n')
        for i, line in enumerate(advice_lines):
            advice_text = font.render(line, True, BLACK)
            screen.blit(advice_text, (10, 100 + i * 40))

        
        if draw_button(screen, "Next", button_x, button_y, button_width, button_height, WHITE, WHITE):
            if day < max_days:
                day += 1
                input_stage = 0
                temperature, weather, soil_moisture, advice = "", "", "", ""
                screen.fill(GREEN)  
            else:
                running = False  

    if draw_button(screen, "Exit", exit_button_x, exit_button_y, button_width, button_height, RED, RED):
        running = False

    pygame.display.flip()

pygame.quit()
sys.exit()

