products_per_category = {
    ("Digital Experience Analytics", 0.33): [
        ("Zone-Based Heatmaps", 0.6),
        ("Journey Analysis", 0.3),
        ("Merchandising", 0.1),
    ],
    ("Digital Experience Monitoring", 0.19): [
        ("Error Analysis", 0.15),
        ("Frustration Scoring", 0.25),
        ("Speed Analysis", 0.6),
    ],
    ("Product Analytics", 0.31): [
        ("Cross-Session", 0.15),
        ("Retention Analytics", 0.2),
        ("User Segments", 0.65)
    ],
    ("Key Capabilities", 0.17): [
        ("Session Replay", 0.3),
        ("Mobile App Analytics", 0.4),
        ("Impact Quantification", 0.3)
    ]
}

regions = {
    ("Europe", 0.3): {
        ("France", 0.23): [
            "Paris", "Marseille", "Lyon", "Toulouse", "Nice"
        ],
        ("Germany", 0.19): [
            "Berlin", "Hamburg", "Munich", "Cologne", "Frankfurt"
        ],
        ("Italy", 0.18): [
            "Rome", "Milan", "Naples", "Turin", "Palermo"
        ],
        ("Spain", 0.18): [
            "Madrid", "Barcelona", "Valencia", "Seville", "Zaragoza"
        ],
        ("United Kingdom", 0.22): [
            "London", "Birmingham", "Manchester", "Glasgow", "Liverpool"
        ]
    },
    ("Asia", 0.15): {
        ("China", 0.28): [
            "Beijing", "Shanghai", "Guangzhou", "Shenzhen", "Chengdu"
        ],
        ("India", 0.18): [
            "New Delhi", "Mumbai", "Bangalore", "Kolkata", "Chennai"
        ],
        ("Japan", 0.22): [
            "Tokyo", "Osaka", "Nagoya", "Yokohama", "Sapporo"
        ],
        ("South Korea", 0.26): [
            "Seoul", "Busan", "Incheon", "Daegu", "Daejeon"
        ],
        ("Saudi Arabia", 0.06): [
            "Riyadh", "Jeddah", "Mecca", "Medina", "Dammam"
        ]
    },
    ("North America", 0.35): {
        ("United States", 0.5): [
            "New York City", "Los Angeles", "Chicago", "Houston", "Phoenix"
        ],
        ("Canada", 0.3): [
            "Toronto", "Montreal", "Vancouver", "Calgary", "Ottawa"
        ],
        ("Mexico", 0.1): [
            "Mexico City", "Guadalajara", "Monterrey", "Puebla", "Tijuana"
        ],
        ("Cuba", 0.05): [
            "Havana", "Santiago de Cuba", "Camagüey", "Holguín", "Santa Clara"
        ],
        ("Jamaica", 0.05): [
            "Kingston", "Montego Bay", "Spanish Town", "Portmore", "May Pen"
        ]
    },
    ("South America", 0.1): {
        ("Brazil", 0.35): [
            "São Paulo", "Rio de Janeiro", "Brasília", "Salvador", "Fortaleza"
        ],
        ("Argentina", 0.3): [
            "Buenos Aires", "Córdoba", "Rosario", "Mendoza", "La Plata"
        ],
        ("Colombia", 0.25): [
            "Bogotá", "Medellín", "Cali", "Barranquilla", "Cartagena"
        ],
        ("Peru", 0.05): [
            "Lima", "Arequipa", "Trujillo", "Chiclayo", "Huancayo"
        ],
        ("Chile", 0.05): [
            "Santiago", "Valparaíso", "Concepción", "Antofagasta", "Viña del Mar"
        ]
    },
    ("Africa", 0.05): {
        ("Nigeria", 0.45): [
            "Lagos", "Kano", "Ibadan", "Kaduna", "Port Harcourt"
        ],
        ("Ethiopia", 0.05): [
            "Addis Ababa", "Dire Dawa", "Mek'ele", "Gondar", "Hawassa"
        ],
        ("Egypt", 0.15): [
            "Cairo", "Alexandria", "Giza", "Port Said", "Suez"
        ],
        ("South Africa", 0.2): [
            "Johannesburg", "Cape Town", "Durban", "Pretoria", "Port Elizabeth"
        ],
        ("Kenya", 0.15): [
            "Nairobi", "Mombasa", "Kisumu", "Nakuru", "Eldoret"
        ]
    }
}

domains = [
    "Commerce de détail et e-commerce",
    "Éducation et formation",
    "Services financiers et bancaires",
    "Santé et soins de santé",
    "Médias et divertissement",
    "Services professionnels (conseil, comptabilité, juridique)",
    "Tourisme et voyage",
    "Automobile et transport",
    "Télécommunications",
    "Sports et loisirs"
]

subscription_prices = [
    "500",
    "1000",
    "2000",
    "5000",
    "10000"
]