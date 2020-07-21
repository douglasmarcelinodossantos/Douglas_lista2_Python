import simulation

if __name__ == '__main__':
    passos = 10
    todas_as_medias = 0
    for i in range(passos):
        sim = simulation.Simulacao()
        todas_as_medias += sim.run_model()
